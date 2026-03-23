import torch
from PIL import Image
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
from qwen_vl_utils import process_vision_info

from util import *


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


def construct_message(QA, image_path):
    message = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_path
                },
                {
                    "type": "text",
                    "text": build_prompt(QA['question'])
                }
            ],
        }
    ]
    return message

def generate_message_qa_list_hard():
    base_path = './'
    message_qa_list = []

    hard_problem_category = ['long_arrow', 'multi_arrow', 'not_right_arrow', 'overlap_arrow']
    for dir in hard_problem_category:
        for i in range(5):
            path = base_path + 'SAD_sythesis/' + dir + '/'

            folder = path + str(i) + '/json_object/'

            names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            file = names[0]

            with open(folder + file, 'r') as f:
                json_object = json.load(f)
            with open(folder.replace('json_object', 'QA') + file.replace('.json', '_QA.json'), "r") as f:
                qa_list = json.load(f)

            image_path = os.path.join(folder.replace('json_object', 'Diagram') , file.replace(".json", ".png"))
            for qa in qa_list:
                # message = construct_message(qa, image_path)
                message_qa_list.append({
                    'QA': qa,
                    'image_path': image_path,
                    'file': file,
                    'diagram_type': 'structural'
                })
    return message_qa_list

def generate_message_qa_list(diagram_type):
    base_path = './'
    message_qa_list = []
    qa_path = base_path + 'SAD/' + diagram_type + '/QA/'
    img_path = base_path + 'SAD/' + diagram_type + '/Diagram/'

    for file in os.listdir(qa_path):
        with open(os.path.join(qa_path, file), "r") as f:
            qa_list = json.load(f)
        image_path = os.path.join(img_path, file.replace("_QA.json", ".png"))

        for qa in qa_list:
            # message = construct_message(qa, image_path)
            message_qa_list.append({
                'QA': qa,
                # 'message': message,
                'image_path': image_path,
                'file': file,
                'diagram_type': diagram_type
            })
    return message_qa_list


def generate_message_qa_list_add(diagram_type):
    base_path = './'
    message_qa_list = []
    qa_path = base_path + 'SAD/' + diagram_type + '/QA/'
    img_path = base_path + 'SAD/' + diagram_type + '/Diagram/'

    for file in os.listdir(qa_path):
        with open(os.path.join(qa_path, file), "r") as f:
            qa_list = json.load(f)
        image_path = os.path.join(img_path, file.replace("_QA.json", ".png"))

        for qa in qa_list:
            # message = construct_message(qa, image_path)
            if qa['metadata']['sub_type'] == 'label_on_the_relation_target':
                message_qa_list.append({
                    'QA': qa,
                    # 'message': message,
                    'image_path': image_path,
                    'file': file,
                    'diagram_type': diagram_type
                })
    return message_qa_list


def generate_output(message_qa, processor, model, settings):
    QA = message_qa["QA"]
    message = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": message_qa["image_path"]},
                {"type": "text", "text": build_prompt(QA["question"])},
            ],
        }
    ]

    # Build prompt string (chat template)
    text = processor.apply_chat_template(
        message, tokenize=False, add_generation_prompt=True
    )

    # Process vision + text
    image_inputs, video_inputs = process_vision_info(message)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    ).to(model.device)

    # ---- Token usage (prompt) ----
    # padding-safe: counts non-pad tokens in the prompt
    # attention_mask is (batch, seq). For batch=1, sum -> scalar.
    prompt_tokens = int(inputs["attention_mask"].sum().item())
    # Generate (ask HF to return dict so we can read sequences robustly)
    with torch.no_grad():
        gen = model.generate(
            **inputs,
            max_new_tokens=settings["max_completion_tokens"],
            do_sample=settings["do_sample"],
            temperature=settings.get("temperature", None),
            top_p=settings.get("top_p", None),
            return_dict_in_generate=True,
            output_scores=False,
        )

    # gen.sequences is (batch, prompt+completion)
    sequences = gen.sequences
    total_tokens = int(sequences.shape[1])
    completion_tokens = int(total_tokens - prompt_tokens)

    # Decode ONLY the newly generated tokens
    decoded = processor.batch_decode(
        sequences[:, prompt_tokens:], skip_special_tokens=True
    )[0]

    usage = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
    }
    return decoded, usage

settings = {
    'model': 'Qwen/Qwen2.5-VL-32B-Instruct',
    'do_sample': False,
    'max_completion_tokens': 512,
}


# Load
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    settings['model'],
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(settings['model'])
diagram_type_list = ['behavior', 'structural', 'ER']
hard_part = True
if hard_part:
    message_qa_list = generate_message_qa_list_hard()
else:
    message_qa_list = []
    for diagram_type in diagram_type_list:
        message_qa_list += generate_message_qa_list(diagram_type)
print(len(message_qa_list), flush=True)
for index, message_qa in enumerate(message_qa_list):
    if index > 0:

        response, usage = generate_output(message_qa, processor, model, settings)
        qa = message_qa["QA"]
        file = message_qa["file"]
        diagram_type = message_qa["diagram_type"]
        res = {
            "index": index,
            "diagram_type": diagram_type,
            "file": file.replace("_QA.json", ""),
            "question": qa["question"],
            "response": response,
            "answer": qa["answer"],
            "metadata": qa["metadata"],
            "setting": settings,
            'token_usage': usage
        }
        print(json.dumps(res), flush=True)