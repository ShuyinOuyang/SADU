import json
import re
import os
import asyncio
import argparse
import mimetypes
import random
from openai import BadRequestError, RateLimitError, APITimeoutError, APIConnectionError
from openai import OpenAI, AsyncOpenAI


base_path = '../../'

def check_counting_or_retrieval(sub_type):
    counting_types = [
        'total_entity_number',
        'total_relation_number',
        'entities_have_more_than_one_relations',
        'total_cluster_number',
        'how_many_entities_not_in_clusters',
        'how_many_relations_have_label',
        'how_many_clusters_have_clusters_within',
        'how_many_entities_does_certain_cluster_have',
        'how_many_relation_types',
        'how_many_attributes_certain_entity_has',
        'how_many_methods_certain_entity_has',
    ]
    retrieval_types = [
        'cluster_has_most_entities',
        'relation_statement',
        'two_entities_in_the_same_cluster',
        'certain_cluster_contains_entity',
        'label_on_the_relation',
        'label_on_the_relation_source',
        'label_on_the_relation_target',
        # 'labeled_relation_between_certain_elements',
        'cluster_contains_certain_entity',
        'entity_contains_certain_attribute',
        'entity_contains_certain_method',
        'type_on_the_relation',
        'relation_source',
        'relation_target',
        'which_relation_has_certain_label'
    ]

    if sub_type in counting_types:
        return 'counting'
    elif sub_type in retrieval_types:
        return 'retrieval'
    else:
        return ''


def build_prompt(response, answer):
    final_prompt = ('You are an expert evaluator for software architecture diagram question-answering tasks. '
                    'Your job is to judge whether the `response` is semantically equivalent to the ground-truth `answer`. \n\n'
                    'Evaluation Rules:\n'
                    '1. For numerical questions:\n'
                    '   - The response is Equivalent only if the number matches exactly.\n\n'
                    '2. For retrieval questions:\n'
                    '   - The response is Equivalent only if it identifies the same entity or set of entities as the ground truth.\n'
                    '   - Different entities, missing entities, or extra entities make the response Not Equivalent.\n\n'
                    '3. Do NOT ignore differences that change meaning:\n'
                    '   - incorrect component names\n'
                    '   - different quantities\n'
                    '   - incorrect relationship direction or type\n'
                    '   - retrieving the wrong entity.\n\n'
                    '4. You must NOT fix, rewrite, or interpret the model\'s output beyond semantic matching.\n\n'
                    'Output Format (MANDATORY):\n'
                    '   - First line should return one of the output label:\n'
                    '       - True\n'
                    '       - False\n'
                    '   - Second line should include one short sentence explaining why.\n\n'
                    'Now evaluate the following:\n\n'
                    '# Response #\n'
                    '%s\n'
                    '# Answer #\n'
                    '%s\n' % (response, answer)
                    )
    return final_prompt


def generate_message_response_obj_list(response_list, existing=[]):
    message_response_obj_list = []

    for response_obj in response_list:
        if response_obj['index'] in existing:
            continue
        answer = response_obj['answer']
        processed_response = response_obj['processed_response']

        input_text = build_prompt(processed_response, answer)

        message = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": input_text},
                ],
            }
        ]
        message_response_obj_list.append({
            'message': message,
            'response_obj': response_obj,
        })

    return message_response_obj_list


def over_length_fix(response):
    # format error fix
    if ('[start]' in response) and ('[end]' not in response):
        idx = response.rfind('",')
        if idx != -1:
            response = response[:idx] + "\"]}\n[end]"
    return response

def json_str_fix(json_str):
    json_str = json_str.strip()
    # Fix 1  }] -> ]}
    if json_str.endswith('}]'):
        json_str = json_str.replace('}]', ']}')
    # Fix 2
    if ', "x1", "x2", ...' in json_str:
        json_str = json_str.replace(', "x1", "x2", ...', '')
    # Fix 3
    if ', "x2", ...' in json_str:
        json_str = json_str.replace(', "x2", ...', '')
    # Fix 4
    if ', ...' in json_str:
        json_str = json_str.replace(', ...', '')

    # Fix 5
    if json_str.startswith('{"answer": "'):
        json_str = json_str.replace('{"answer": "', '{"answer": ["')
    if json_str.endswith('"}') or json_str.endswith('" }'):
        json_str = json_str.replace('"}', '"]}').replace('" }', '"]}')

    return json_str

def response_processing(response):
    # response -> valid json str
    response = over_length_fix(response)  # format error fix
    match = re.search(r'\[start\](.*?)\[end\]', response, flags=re.S)
    if match:
        json_str = match.group(1).strip()  # remove whitespace
    else:
        return 'format_error'
        # classification['format_wrong'].append(i)

    json_str = json_str_fix(json_str)
    try:
        obj = json.loads(json_str)
    except:
        return 'json_error'

    if 'answer' in obj:
        if isinstance(obj['answer'], list):
            obj['answer'] = sorted(list(obj['answer']))
            json_str = json.dumps(obj)
    else:
        return 'json_key_error'

    return json_str


class EmptyJudgeResponseError(RuntimeError):
    pass

def _normalize_judge_text(text: str) -> str:
    # Strip + keep at most 2 lines
    t = (text or "").strip()
    if not t:
        return ""
    lines = t.splitlines()
    if len(lines) > 2:
        t = "\n".join(lines[:2]).strip()
    return t

def _is_valid_judge_text(t: str) -> bool:
    # Expect first line to be True/False (case-insensitive)
    if not t:
        return False
    first = t.splitlines()[0].strip().lower()
    return first in {"true", "false"}

async def run_one(client, index, message_response_obj, settings, sem):
    message = message_response_obj["message"]
    response_obj = message_response_obj["response_obj"]

    max_tokens = settings.get("max_completion_tokens", 128)
    max_tokens_cap = settings.get("max_completion_tokens_cap", 1024)

    max_attempts = settings.get("max_attempts", 6)
    base_delay = settings.get("base_retry_delay_sec", 0.8)

    async with sem:
        last_err = None
        for attempt in range(1, max_attempts + 1):
            try:
                chat_completion = await client.chat.completions.create(
                    model=settings["model"],
                    messages=message,
                    max_completion_tokens=max_tokens,
                    temperature=settings.get("temperature", 0),
                )

                raw = chat_completion.choices[0].message.content
                judge_text = _normalize_judge_text(raw)

                # NEW: retry if empty or malformed
                if not judge_text:
                    raise EmptyJudgeResponseError("Empty judge_response from model.")
                if not _is_valid_judge_text(judge_text):
                    raise EmptyJudgeResponseError(f"Malformed judge_response: {judge_text!r}")

                res = {
                    "index": index,
                    "judge_response": judge_text,
                    "response_obj": response_obj,
                    "message": message,
                }
                print(json.dumps(res, ensure_ascii=False), flush=True)
                return

            except EmptyJudgeResponseError as e:
                # Retry with backoff; optionally raise token budget a bit
                last_err = str(e)
                if max_tokens < max_tokens_cap:
                    max_tokens = min(max_tokens * 2, max_tokens_cap)

            except BadRequestError as e:
                msg = str(e)
                last_err = msg
                if "max_tokens" in msg or "output limit" in msg:
                    if max_tokens < max_tokens_cap:
                        max_tokens = min(max_tokens * 2, max_tokens_cap)
                    else:
                        break
                elif "context_length" in msg or "maximum context" in msg:
                    user_text = message[0]["content"][0]["text"]
                    message[0]["content"][0]["text"] = _truncate_for_judge(user_text, max_chars=4000)
                else:
                    break

            except (RateLimitError, APITimeoutError, APIConnectionError) as e:
                last_err = str(e)

            delay = base_delay * (2 ** (attempt - 1)) + random.random() * 0.25
            await asyncio.sleep(min(delay, 20.0))

        # After retries, emit an error record (not empty)
        res = {
            "index": index,
            "judge_response": f"ERROR\nRequest failed after retries: {last_err}",
            "response_obj": response_obj,
            "message": message,
        }
        print(json.dumps(res, ensure_ascii=False), flush=True)
        return

# async def run_all(client, message_response_obj_list, settings):
#     tasks = [
#         run_one(client, message_response_obj['response_obj']['index'], message_response_obj, settings)
#         for i, message_response_obj in enumerate(message_response_obj_list)
#     ]
#
#     # This runs all requests concurrently (within your rate limits)
#     await asyncio.gather(*tasks)

async def run_all(client, message_response_obj_list, settings):
    concurrency = settings.get("concurrency", 16)
    sem = asyncio.Semaphore(concurrency)

    tasks = [
        run_one(client, m['response_obj']['index'], m, settings, sem)
        for m in message_response_obj_list
    ]

    # Critical: never let one exception kill the entire batch
    await asyncio.gather(*tasks, return_exceptions=True)


def evaluation(target, log):

    settings = {
        'model': 'gpt-5.4',
        'temperature': 0,
        'flag_async': True,
        'max_completion_tokens': 256
    }

    with open(base_path + 'personal_token/gpt_info.json', 'r') as f:
        info_dic = json.load(f)


    if settings['flag_async']:
        client = AsyncOpenAI(
            api_key=info_dic['api_key'],
            # http_client = DefaultAioHttpClient(),
        )
    else:
        client = OpenAI(
            api_key=info_dic['api_key']
        )

    # target_file = base_path+'experiment_result/response_result/claude_sonnet_4.5_response_0203_t_0.log'
    # log_file = base_path+'experiment_result/evaluation_result/claude_sonnet_4.5_judge_0203_t_0.log1'

    target_file = base_path + 'experiment_result/response_result/%s' % (target)

    log_file = base_path + 'experiment_result/evaluation_result/%s' % (log)

    existing = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            for line in f.readlines():
                existing.append(json.loads(line)['index'])

    response_list = []
    with open(target_file, 'r') as f:
        for line in f.readlines():
            content = json.loads(line)

            # response preprocess
            if content['response']:
                tmp_response = response_processing(content['response'])
            else:
                tmp_response = ''
            if tmp_response in ['format_error', 'json_error', 'json_key_error']:
                content['processed_response'] = content['response']
            else:
                content['processed_response'] = tmp_response

            response_list.append(content)

    message_response_obj_list = generate_message_response_obj_list(response_list, existing)

    asyncio.run(run_all(client, message_response_obj_list, settings))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        help="Choose target file",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--log",
        type=str,
        help="Choose log file",
        required=True,
    )
    args = parser.parse_args()
    evaluation(args.target, args.log)


# nohup python evaluation_llm_based.py -t "different_prompt/only_question_gemini-3.1-flash-lite-preview_response_0306_t_0.log" -l "judge.log" &> ../../experiment_result/evaluation_result/different_prompt/only_question_gemini-3.1-flash-lite-preview_response_0306_t_0.log &
