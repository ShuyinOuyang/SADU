import anthropic
import json
import base64
import os
from pathlib import Path
import asyncio
from util import *
import asyncio
import random
import time
from collections import deque
import argparse


base_path = '../../'

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.standard_b64encode(image_file.read()).decode("utf-8")

    # Determine media type based on file extension
    extension = Path(image_path).suffix.lower()
    media_type_map = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    media_type = media_type_map.get(extension, 'image/png')

    return encoded, media_type

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

def construct_message(QA, image_path, prompt_type):
    image_data, media_type = encode_image(image_path)
    if prompt_type == 'full':
        message = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": build_prompt(QA['question'])
                    }
                ],
            }
        ]
    elif prompt_type == 'without_definition':
        message = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": build_prompt_without_definition(QA['question'])
                    }
                ],
            }
        ]
    elif prompt_type == 'without_rules':
        message = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": build_prompt_without_rules(QA['question'])
                    }
                ],
            }
        ]
    else:
        message = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": build_prompt_only_question(QA['question'])
                    }
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


# old version
# async def run_one(index, x, settings):
#     completion = await client.messages.create(
#         model=settings['model'],
#         max_tokens=settings['max_completion_tokens'],
#         messages=x['message'],
#         temperature=settings['temperature']
#     )
#
#     qa = x['QA']
#     file = x['file']
#     diagram_type = x['diagram_type']
#
#     res = {
#         "index": index,
#         "diagram_type": diagram_type,
#         "file": file.replace("_QA.json", ""),
#         "question": qa["question"],
#         "response": completion.content[0].text,
#         "answer": qa["answer"],
#         "metadata": qa["metadata"],
#     }
#     print(json.dumps(res), flush=True)
#
# async def run_all(message_qa_list, settings):
#     tasks = [
#         run_one(i, message_qa, settings)
#         for i, message_qa in enumerate(message_qa_list)
#     ]
#
#     # This runs all requests concurrently (within your rate limits)
#     await asyncio.gather(*tasks)


def request_and_print():
    for index, x in enumerate(message_qa_list):
        # if ignore_existing and index in existing:
        #     continue
        completion = client.messages.create(
            model=settings['model'],
            max_tokens=settings['max_completion_tokens'],
            messages=x['message'],
            temperature=settings['temperature'],
        )

        qa = x['QA']
        file = x['file']
        diagram_type = x['diagram_type']

        res = {
            "index": index,
            "diagram_type": diagram_type,
            "file": file.replace("_QA.json", ""),
            "question": qa["question"],
            "response": completion.content[0].text,
            "answer": qa["answer"],
            "metadata": qa["metadata"],
            "setting": settings,
        }
        print(json.dumps(res), flush=True)

class RollingWindowRateLimiter:
    def __init__(self, max_calls: int, period_s: float = 60.0):
        self.max_calls = int(max_calls)
        self.period_s = float(period_s)
        self._calls = deque()
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        """
        Ensure no more than `max_calls` are started within any `period_s` window.
        """
        while True:
            async with self._lock:
                now = time.monotonic()

                # Drop calls older than the window
                while self._calls and (now - self._calls[0]) >= self.period_s:
                    self._calls.popleft()

                if len(self._calls) < self.max_calls:
                    self._calls.append(now)
                    return

                sleep_for = self.period_s - (now - self._calls[0])

            # Sleep outside the lock
            await asyncio.sleep(max(0.0, sleep_for))


def _get_status_code(exc: Exception):
    # Anthropic SDK: APIStatusError subclasses usually expose `.status_code`
    return getattr(exc, "status_code", None)

def _is_retryable_error(exc: Exception) -> bool:
    """
    Retry on:
      - 429 (rate limit)
      - 408/409/425 (transient-ish)
      - 5xx (server errors like your 500)
      - network / timeout errors (APIConnectionError / APITimeoutError)
    """

    # Explicit SDK exception types (best signal)
    if isinstance(exc, (anthropic.RateLimitError, anthropic.APITimeoutError, anthropic.APIConnectionError)):
        return True
    if isinstance(exc, anthropic.APIStatusError):
        sc = exc.status_code
        return sc == 429 or sc >= 500 or sc in (408, 409, 425)

    # Fallback: status_code attribute or message heuristics
    sc = _get_status_code(exc)
    if sc is not None:
        return sc == 429 or sc >= 500 or sc in (408, 409, 425)

    msg = str(exc).lower()
    return any(k in msg for k in ["rate limit", "too many requests", "timeout", "temporarily", "internal server error", "503", "502", "500"])



# def _is_rate_limit_error(exc: Exception) -> bool:
#     """
#     Best-effort check across common SDKs.
#     Adjust if your client exposes a specific exception type.
#     """
#     # Many SDKs expose status_code or have message containing "rate limit"
#     status = getattr(exc, "status_code", None) or getattr(getattr(exc, "response", None), "status_code", None)
#     if status == 429:
#         return True
#     msg = str(exc).lower()
#     return "rate limit" in msg or "too many requests" in msg or "429" in msg

# async def run_one(index, x, settings):
#     # Retry loop for transient 429s
#     max_retries = settings.get("max_retries", 6)
#     base_backoff = settings.get("base_backoff_s", 0.8)  # initial delay
#     max_backoff = settings.get("max_backoff_s", 20.0)
#
#     for attempt in range(max_retries + 1):
#         try:
#             completion = await client.messages.create(
#                 model=settings["model"],
#                 max_tokens=settings["max_completion_tokens"],
#                 messages=x["message"],
#                 temperature=settings["temperature"],
#             )
#
#             qa = x["QA"]
#             file = x["file"]
#             diagram_type = x["diagram_type"]
#
#             res = {
#                 "index": index,
#                 "diagram_type": diagram_type,
#                 "file": file.replace("_QA.json", ""),
#                 "question": qa["question"],
#                 "response": completion.content[0].text,
#                 "answer": qa["answer"],
#                 "metadata": qa["metadata"],
#                 "setting": settings,
#             }
#             print(json.dumps(res), flush=True)
#             return
#
#         except Exception as e:
#             if _is_rate_limit_error(e) and attempt < max_retries:
#                 # Exponential backoff with jitter
#                 backoff = min(max_backoff, base_backoff * (2 ** attempt))
#                 backoff *= random.uniform(0.8, 1.2)
#                 await asyncio.sleep(backoff)
#                 continue
#             raise

async def run_one(index, x, settings, client):
    max_retries = settings.get("max_retries", 6)
    base_backoff = settings.get("base_backoff_s", 0.8)
    max_backoff = settings.get("max_backoff_s", 20.0)

    qa = x["QA"]
    file = x["file"]
    diagram_type = x["diagram_type"]

    for attempt in range(max_retries + 1):
        try:
            completion = await client.messages.create(
                model=settings["model"],
                max_tokens=settings["max_completion_tokens"],
                messages=x["message"],
                temperature=settings["temperature"],
            )

            res = {
                "index": index,
                "diagram_type": diagram_type,
                "file": file.replace("_QA.json", ""),
                "question": qa["question"],
                "response": completion.content[0].text,
                "answer": qa["answer"],
                "metadata": qa["metadata"],
                "setting": settings,
                "token_usage": {
                    "prompt_tokens": completion.usage.input_tokens,
                    "completion_tokens": completion.usage.output_tokens,
                    "total_tokens": completion.usage.input_tokens + completion.usage.output_tokens
                }
            }
            # print(completion.usage, flush=True)
            print(json.dumps(res), flush=True)
            return

        except Exception as e:
            if _is_retryable_error(e) and attempt < max_retries:
                backoff = min(max_backoff, base_backoff * (2 ** attempt))
                backoff *= random.uniform(0.8, 1.2)
                await asyncio.sleep(backoff)
                continue

            # Final failure: DO NOT raise -> keep the whole script alive
            err_res = {
                "index": index,
                "diagram_type": diagram_type,
                "file": file.replace("_QA.json", ""),
                "question": qa.get("question"),
                "error": {
                    "type": type(e).__name__,
                    "status_code": getattr(e, "status_code", None),
                    "message": str(e),
                    "request_id": getattr(e, "request_id", None) or getattr(getattr(e, "response", None), "headers", {}).get("request-id"),
                },
                "setting": settings,
            }
            print(json.dumps(err_res), flush=True)
            return

async def run_all(message_qa_list, settings, existing, client):
    rpm = settings.get("requests_per_minute", 60)
    workers = settings.get("max_concurrency", 5)

    limiter = RollingWindowRateLimiter(max_calls=rpm, period_s=60.0)

    queue = asyncio.Queue()
    for i, item in enumerate(message_qa_list):
        if i not in existing:
            queue.put_nowait((i, item))

    async def worker_loop():
        while True:
            try:
                i, item = queue.get_nowait()
            except asyncio.QueueEmpty:
                return

            try:
                await limiter.acquire()
                await run_one(i, item, settings, client)
            finally:
                queue.task_done()

    await asyncio.gather(*(worker_loop() for _ in range(workers)))

# async def run_all(message_qa_list, settings, existing):
#     rpm = settings.get("requests_per_minute", 60)       # set to your limit
#     workers = settings.get("max_concurrency", 5)        # in-flight requests
#
#     limiter = RollingWindowRateLimiter(max_calls=rpm, period_s=60.0)
#
#     queue = asyncio.Queue()
#     for i, item in enumerate(message_qa_list):
#         if i not in existing:
#             queue.put_nowait((i, item))
#
#     async def worker_loop():
#         while True:
#             try:
#                 i, item = queue.get_nowait()
#             except asyncio.QueueEmpty:
#                 return
#
#             # Important: rate-limit right before making the request
#             await limiter.acquire()
#             await run_one(i, item, settings)
#             queue.task_done()
#
#     await asyncio.gather(*(worker_loop() for _ in range(workers)))


# def main(model, temperature):
with open(base_path + 'personal_token/claude_info.json', 'r') as f:
    info_dic = json.load(f)

diagram_type_list = ['behavior', 'structural', 'ER']

# hard_part = False
hard_part = False

settings = {
    'model': 'claude-haiku-4-5',
    # 'model': 'claude-sonnet-4-5',
    'temperature': 0,
    'flag_async': True,
    'max_completion_tokens': 512,

    "requests_per_minute": 50,  # choose below your actual RPM limit
    "max_concurrency": 5,

    # Retry controls
    "max_retries": 6,
    "base_backoff_s": 0.8,
    "max_backoff_s": 20.0,

    # 'prompt_type': 'full',
    # 'prompt_type': 'without_definition',
    'prompt_type': 'without_rules',
    # 'prompt_type': 'only_question',
}


# settings = {
#     'model': model,
#     'temperature': temperature,
#     'flag_async': True,
#     'max_completion_tokens': 256,
#     "requests_per_minute": 50,
#     "max_concurrency": 5,
#     "max_retries": 6,
#     "base_backoff_s": 0.8,
#     "max_backoff_s": 20.0,
# }

log_file = base_path + 'experiment_result/response_result/test.log'
existing = []
if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        for line in f.readlines():
            existing.append(json.loads(line)['index'])

if hard_part:
    message_qa_list = generate_message_qa_list_hard()
else:
    message_qa_list = []
    for diagram_type in diagram_type_list:
        message_qa_list += generate_message_qa_list(diagram_type, settings['prompt_type'])


# if settings['flag_async']:
#     client = anthropic.AsyncAnthropic(api_key=info_dic['api_key'], http_client=anthropic.DefaultAioHttpClient(),)
#     asyncio.run(run_all(message_qa_list, settings, existing, client))
# else:
#     client = anthropic.Anthropic(api_key=info_dic['api_key'])
#     request_and_print()

# message_qa_list = generate_message_qa_list_hard()


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "-f",
#         "--function",
#         type=str,
#         choices=['generate_ground_truth_code', 'compilation_filter', 'deduplication'],
#         help="Choose script function",
#         required=True,
#     )
#     parser.add_argument(
#         "-s",
#         "--source",
#         type=str,
#         choices=['ds1000', 'stackoverflow'],
#         help="Choose seed code source",
#         required=True,
#     )
#     parser.add_argument(
#         "-l",
#         "--library",
#         type=str,
#         choices=['numpy', 'pandas', 'matplotlib', 'scipy', 'sklearn',
#                  'tensorflow', 'pytorch', 'seaborn', 'keras', 'lightgbm'],
#         help="Choose library",
#         default='numpy'
#     )