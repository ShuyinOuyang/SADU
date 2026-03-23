import json
import os
import asyncio
from google import genai
from pathlib import Path
from google.genai import types
from aiohttp.client_exceptions import ClientConnectorError

from util import *

base_path = '../../'



def construct_message(QA, image_path, prompt_type):
    image_bytes = Path(image_path).read_bytes()
    types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/png",
    ),
    if prompt_type == 'full':
        message = [
            build_prompt(QA['question']),
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            ),
        ]
    elif prompt_type == 'without_definition':
        message = [
            build_prompt_without_definition(QA['question']),
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            ),
        ]
    elif prompt_type == 'without_rules':
        message = [
            build_prompt_without_rules(QA['question']),
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            ),
        ]
    else:
        message = [
            build_prompt_only_question(QA['question']),
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            ),
        ]
    return message

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
                message = construct_message(qa, image_path, 'full')
                message_qa_list.append({
                    'QA': qa,
                    'message': message,
                    'file': file,
                    'diagram_type': 'structural'
                })
    return message_qa_list

def generate_message_qa_list(diagram_type, prompt_type):
    message_qa_list = []
    qa_path = base_path + 'dataset/SAD/' + diagram_type + '/QA/'
    img_path = base_path + 'dataset/SAD/' + diagram_type + '/Diagram/'

    for file in os.listdir(qa_path):
        with open(os.path.join(qa_path, file), "r") as f:
            qa_list = json.load(f)
        image_path = os.path.join(img_path, file.replace("_QA.json", ".png"))

        for qa in qa_list:
            message = construct_message(qa, image_path, prompt_type)
            message_qa_list.append({
                'QA': qa,
                'message': message,
                'file': file,
                'diagram_type': diagram_type
            })
    return message_qa_list


async def run_one_gemini(index, message_qa, settings):
    # response = await client.models.generate_content(
    try:
        if 'thinking_level' in settings:
            response = await client.aio.models.generate_content(
                model=settings["model"],
                contents=message_qa['message'],
                config=types.GenerateContentConfig(
                    max_output_tokens=settings["max_completion_tokens"],
                    temperature=settings["temperature"],
                    thinking_config=types.ThinkingConfig(
                        thinking_level=settings["thinking_level"],
                    ),
                ),
            )
        else:
            response = await client.aio.models.generate_content(
                model=settings["model"],
                contents=message_qa['message'],
                config=types.GenerateContentConfig(
                    max_output_tokens=settings["max_completion_tokens"],
                    temperature=settings["temperature"],
                ),
            )

        qa = message_qa['QA']
        file = message_qa['file']
        diagram_type = message_qa['diagram_type']
        if response.text:
            response_text = response.text
        else:
            response_text = ''
        res = {
            "index": index,
            "diagram_type": diagram_type,
            "file": file.replace("_QA.json", ""),
            "question": qa["question"],
            "response": response_text,
            "answer": qa["answer"],
            "metadata": qa["metadata"],
            "setting": settings,
            "token_usage": {
                "prompt_tokens": response.usage_metadata.prompt_token_count,
                "thoughts_token": response.usage_metadata.thoughts_token_count,
                "completion_tokens": response.usage_metadata.candidates_token_count,
                "cached_content_tokens": response.usage_metadata.cached_content_token_count,
                "total_tokens": response.usage_metadata.total_token_count
            }
        }
        # print(response.usage_metadata, flush=True)
        print(json.dumps(res), flush=True)
    except Exception as e:
        # print(e)
        pass

async def run_all_gemini(message_qa_list, settings, existing):
    tasks = [
        run_one_gemini(i, message_qa, settings)
        for i, message_qa in enumerate(message_qa_list) if i not in existing
    ]
    await asyncio.gather(*tasks)

def request_and_print():
    for index, message_qa in enumerate(message_qa_list):
        response = client.models.generate_content(
            model=settings["model"],
            contents=message_qa['message'],
            config=types.GenerateContentConfig(
                max_output_tokens=settings["max_completion_tokens"],
                temperature=settings["temperature"],
            ),
        )
        qa = message_qa['QA']
        file = message_qa['file']
        diagram_type = message_qa['diagram_type']
        res = {
            "index": index,
            "diagram_type": diagram_type,
            "file": file.replace("_QA.json", ""),
            "question": qa["question"],
            "response": response.text,
            "answer": qa["answer"],
            "metadata": qa["metadata"],
            "setting": settings,
        }
        print(json.dumps(res), flush=True)

with open(base_path + 'personal_token/gemini_info.json', 'r') as f:
    info_dic = json.load(f)

diagram_type_list = ['behavior', 'structural', 'ER']

settings = {
    # 'model': 'gemini-2.5-flash-lite',
    # 'model': 'gemini-2.5-flash',
    # 'model': 'gemini-3-flash-preview',
    'model': 'gemini-3.1-flash-lite-preview',
    'temperature': 0,
    'flag_async': True,
    'max_completion_tokens': 512,
    'prompt_type': 'full',
    # 'prompt_type': 'without_definition',
    # 'prompt_type': 'without_rules',
    # 'prompt_type': 'only_question',
    # 'thinking_level': "minimal",
    # 'thinking_level': "low",
    # 'thinking_level': 'medium',
    # 'thinking_level': "high",
}

client = genai.Client(api_key=info_dic['api_key'])

log_file = base_path+'experiment_result/response_result/test.log'

existing = []
if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        for line in f.readlines():
            existing.append(json.loads(line)['index'])

hard_part = False
if hard_part:
    message_qa_list = generate_message_qa_list_hard()
else:
    message_qa_list = []
    for diagram_type in diagram_type_list:
        message_qa_list += generate_message_qa_list(diagram_type, settings['prompt_type'])

if settings["flag_async"]:
    asyncio.run(run_all_gemini(message_qa_list, settings, existing))
    pass
else:
    # request_and_print()
    pass
