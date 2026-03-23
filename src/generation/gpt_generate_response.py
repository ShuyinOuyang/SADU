import json
import base64
import re
import os
import random
import time
import asyncio
import mimetypes
from openai import OpenAI, AsyncOpenAI
from util import *
from typing import Optional
from openai import APITimeoutError, APIConnectionError, RateLimitError, APIError


base_path = '../../'
# generate prompt


def _extract_content(chat_completion) -> str:
    """
    Safely extract model text from ChatCompletions response.
    Returns "" if missing.
    """
    try:
        choices = getattr(chat_completion, "choices", None) or []
        if not choices:
            return ""
        msg = getattr(choices[0], "message", None)
        if msg is None:
            return ""
        content = getattr(msg, "content", None)
        return content if isinstance(content, str) else ""
    except Exception:
        return ""

def _is_valid_output(text: str) -> bool:
    """
    Define what 'valid output' means for your task.
    Minimal: non-empty after stripping.
    You can strengthen this (e.g., must contain '{' if you expect JSON).
    """
    return bool(text and text.strip())

async def _sleep_backoff(attempt: int, base: float = 0.8, cap: float = 20.0) -> None:
    """
    Exponential backoff with jitter.
    attempt starts from 1.
    """
    delay = min(cap, base * (2 ** (attempt - 1)))
    delay = delay * (0.7 + 0.6 * random.random())  # jitter in [0.7, 1.3]
    await asyncio.sleep(delay)

async def _chat_create_with_retries(
    client,
    *,
    model: str,
    messages,
    max_completion_tokens: int,
    temperature: float,
    request_timeout_s: float,
    max_attempts: int = 6,
) -> str:
    """
    Retries on:
      - timeouts / connection errors / transient API errors / rate limits
      - empty outputs (your requirement)
    """
    last_err: Optional[Exception] = None

    for attempt in range(1, max_attempts + 1):
        try:
            # Per-request timeout: use with_options if available
            # (works on current OpenAI python SDK)
            _client = client.with_options(timeout=request_timeout_s)

            chat_completion = await _client.chat.completions.create(
                model=model,
                messages=messages,
                max_completion_tokens=max_completion_tokens,
                temperature=temperature,
            )

            text = _extract_content(chat_completion)

            # Your requirement: do not accept empty output
            if _is_valid_output(text):
                return text

            last_err = ValueError("Empty/invalid model output")
        except (APITimeoutError, APIConnectionError, RateLimitError) as e:
            last_err = e
        except APIError as e:
            # Many APIError are transient (5xx). Retry.
            last_err = e
        except asyncio.CancelledError:
            # If the whole run is being cancelled, respect it
            raise
        except Exception as e:
            # Unexpected errors: retry a couple times, then give up
            last_err = e

        if attempt < max_attempts:
            await _sleep_backoff(attempt)

    # After all retries exhausted:
    raise last_err if last_err is not None else RuntimeError("Failed without explicit error")


def construct_message(QA, image_path):
    mime, _ = mimetypes.guess_type(image_path)
    if mime is None:
        mime = "image/png"
    with open(image_path, "rb") as image_file:
        b64_image = base64.standard_b64encode(image_file.read()).decode("utf-8")
    message = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": build_prompt(QA['question'])},
                {"type": "image_url", "image_url": {'url': f"data:{mime};base64,{b64_image}", "detail": "low"}},
                # {"type": "image_url", "image_url": f"data:{mime};base64,{b64_image}", "detail": "low"},
            ],
        }
    ]
    return message

def generate_message_qa_list_add(diagram_type):
    message_qa_list = []
    qa_path = base_path + 'dataset/SAD/' + diagram_type + '/QA/'
    img_path = base_path + 'dataset/SAD/' + diagram_type + '/Diagram/'

    for file in os.listdir(qa_path):
        with open(os.path.join(qa_path, file), "r") as f:
            qa_list = json.load(f)
        image_path = os.path.join(img_path, file.replace("_QA.json", ".png"))

        for qa in qa_list:
            if qa['metadata']['sub_type'] == 'label_on_the_relation_target':
                message = construct_message(qa, image_path)
                message_qa_list.append({
                    'QA': qa,
                    'message': message,
                    'file': file,
                    'diagram_type': diagram_type
                })
    return message_qa_list

def generate_message_qa_list_hard():
    message_qa_list = []

    hard_problem_category = ['long_arrow', 'multi_arrow', 'not_right_arrow', 'overlap_arrow']
    for dir in hard_problem_category:
        for i in range(5):
            path = base_path + 'dataset/SAD_sythesis/' + dir + '/'

            folder = path + str(i) + '/json_object/'

            names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            file = names[0]

            with open(folder + file, 'r') as f:
                json_object = json.load(f)
            with open(folder.replace('json_object', 'QA') + file.replace('.json', '_QA.json'), "r") as f:
                qa_list = json.load(f)

            image_path = os.path.join(folder.replace('json_object', 'Diagram') , file.replace(".json", ".png"))
            for qa in qa_list:
                message = construct_message(qa, image_path)
                message_qa_list.append({
                    'QA': qa,
                    'message': message,
                    'file': file,
                    'diagram_type': 'structural'
                })
    return message_qa_list

def generate_message_qa_list(diagram_type):
    message_qa_list = []
    qa_path = base_path + 'dataset/SAD/' + diagram_type + '/QA/'
    img_path = base_path + 'dataset/SAD/' + diagram_type + '/Diagram/'

    for file in os.listdir(qa_path):
        with open(os.path.join(qa_path, file), "r") as f:
            qa_list = json.load(f)
        image_path = os.path.join(img_path, file.replace("_QA.json", ".png"))

        for qa in qa_list:
            message = construct_message(qa, image_path)
            message_qa_list.append({
                'QA': qa,
                'message': message,
                'file': file,
                'diagram_type': diagram_type
            })
    return message_qa_list


async def run_one_gpt(index, message_qa, settings):
    try:
        chat_completion = await client.chat.completions.create(
            model=settings['model'],
            messages=message_qa['message'],
            # max_completion_tokens=settings['max_completion_tokens'],
            temperature=settings['temperature'],
        )

        qa = message_qa['QA']
        file = message_qa['file']
        diagram_type = message_qa['diagram_type']
        res = {
            "index": index,
            "diagram_type": diagram_type,
            "file": file.replace("_QA.json", ""),
            "question": qa["question"],
            "response": chat_completion.choices[0].message.content,
            "answer": qa["answer"],
            "metadata": qa["metadata"],
            "setting": settings,
            "token_usage": {
                "prompt_tokens": chat_completion.usage.prompt_tokens,
                "completion_tokens": chat_completion.usage.completion_tokens,
                "total_tokens": chat_completion.usage.total_tokens
            }
        }
        # print(chat_completion)
        print(json.dumps(res), flush=True)
    except Exception as e:
        pass

async def run_all_gpt(message_qa_list, settings, existing):
    tasks = [
        run_one_gpt(i, message_qa, settings)
        for i, message_qa in enumerate(message_qa_list) if i not in existing
    ]
    # This runs all requests concurrently (within your rate limits)
    await asyncio.gather(*tasks)


diagram_type_list = ['behavior', 'structural', 'ER']
# diagram_type_list = ['behavior']

settings = {
    # 'model': 'gpt-4o-mini',
    'model': 'gpt-5-nano',
    'temperature': 1,
    'flag_async': True,
    'max_completion_tokens': 512
}


if 'gpt' in settings['model']:
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

    hard_part = False
    if hard_part:
        message_qa_list = generate_message_qa_list_hard()
    else:
        message_qa_list = []
        for diagram_type in diagram_type_list:
            message_qa_list += generate_message_qa_list(diagram_type)

    log_file = base_path + 'experiment_result/response_result/test.log'
    existing = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            for line in f.readlines():
                existing.append(json.loads(line)['index'])

    asyncio.run(run_all_gpt(message_qa_list, settings, existing))