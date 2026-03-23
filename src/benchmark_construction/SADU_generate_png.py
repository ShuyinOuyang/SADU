import json
import os
import cairosvg
import subprocess
from pdf2image import convert_from_path
from typing import Dict, Any, List, Tuple

base_path = '../../'

def pdf2png(source_file, target_file, dpi=200):
    images = convert_from_path(source_file, dpi=dpi)
    # Save first page
    images[0].save(target_file, "PNG")

    # pages = convert_from_path(source_file)
    # for i, page in enumerate(pages):
    #     page.save(target_file, "PNG", dpi=dpi)


def svg2png(source_file, target_file, dpi=300):
    # cairosvg.svg2png(url=dataset_path + '/' + file, write_to=dataset_path + '/' + file.replace('.svg', '.png'))
    cairosvg.svg2png(url=source_file, write_to=target_file, dpi=dpi)


CARD_TO_SYMBOL = {
    # Mermaid crow's-foot: leftSymbols--rightSymbols
    # |  = exactly one
    # o  = zero or one
    # {  = one or more  (right side only, paired with | or o on left)
    # }  = zero or more (right side only, paired with | or o on left)
    "exactly one": "||",
    "zero or one": "o|",   # Mermaid uses 'o' at the outer end; '|' towards entity
    "one or more":  "|{",
    "zero or more": "o{",
}

def normalize_type(t):
    """Keep the original DB-ish type for readability."""
    return t

def format_attribute(attr):
    """
    Input: [dtype, name, keyFlag, comment]
    Output line for Mermaid ER attributes block: "dtype name PK|FK"
    """
    dtype, name, key, _comment = (attr + ["", "", "", ""])[:4]
    dtype_out = normalize_type(dtype)
    key_tag = key.strip().upper()
    suffix = f" {key_tag}" if key_tag in {"PK", "FK", "UK"} else ""
    return f"    {dtype_out} {name}{suffix}"

def make_entity_block(name, attributes):
    lines = [f"  \"{name}\" {{"]  # Mermaid wants the entity name then a block
    for a in attributes:
        lines.append(format_attribute(a))
    lines.append("  }")
    return "\n".join(lines)

def make_relation_line(src_name: str, dst_name: str, rel_name: str,
                       src_card: str, dst_card: str) -> str:
    """
    Build lines like:
      A ||--o{ B : "label"
    """
    s_sym = CARD_TO_SYMBOL.get(src_card, "||")
    d_sym = CARD_TO_SYMBOL.get(dst_card, "||")

    # Mermaid expects the two-end symbols around the -- connector,
    # e.g., ||--o{  (sourceSymbols -- targetSymbols)
    return f'  \"{src_name}\" {s_sym}--{d_sym} \"{dst_name}\" : "{rel_name}"'

def json_to_mermaid(data: Dict[str, Any]) -> str:
    ents: Dict[str, Dict[str, Any]] = data.get("entity", {})
    rels: List[Dict[str, Any]] = data.get("relation", [])

    # Map internal ids (entity_0, ...) -> display names (tournament, ...)
    id_to_name: Dict[str, str] = {}
    for eid, edef in ents.items():
        raw = edef.get("name", eid)
        safe = raw.replace(" ", "_")  # Mermaid entity identifiers should avoid spaces
        id_to_name[eid] = safe

    out: List[str] = ["erDiagram"]

    # Entities first
    for eid, edef in ents.items():
        ename = id_to_name[eid]
        attrs = edef.get("attribute", [])
        out.append(make_entity_block(ename, attrs))

    # Then relations
    for r in rels:
        src = id_to_name.get(r["source"], r["source"])
        dst = id_to_name.get(r["target"], r["target"])
        rel_name = r.get("name", "")
        src_card = r.get("source_cardinality", "exactly one")
        dst_card = r.get("target_cardinality", "zero or more")
        out.append(make_relation_line(src, dst, rel_name, src_card, dst_card))

    return "\n".join(out)


def generate_canaidates():
    folder = './dataset/SAD/'
    diagram_types = ['behavior', 'structural', 'ER']
    candidate_list = []
    for diagram_type in diagram_types:
        file_list = os.listdir(folder + diagram_type + '/json_object/')
        easy_count = 0
        medium_count = 0
        difficult_count = 0
        for file in file_list:
            if file == 'baseline-azure-ai-foundry.json':
                continue
            if file == 'multiple-regions-api-management-multiple-after.json':
                continue
            print(easy_count, medium_count, difficult_count)
            if easy_count == 2 and medium_count == 2 and difficult_count == 2:
                break
            if file.endswith('.json'):
                file_path = folder + diagram_type + '/json_object/' + file
                with open(file_path, 'r') as f:
                    json_object = json.load(f)
                if json_object['difficulty'] == 'easy' and easy_count < 2:
                    candidate_list.append(file_path)
                    easy_count += 1
                elif json_object['difficulty'] == 'medium' and medium_count < 2:
                    candidate_list.append(file_path)
                    medium_count += 1
                elif json_object['difficulty'] == 'difficult' and difficult_count < 2:
                    candidate_list.append(file_path)
                    difficult_count += 1
    return candidate_list
# path = 'dataset/SAD_backup/structural/classDiagram/'
# target_folder = 'dataset/SAD/structural/Diagram/'
#
# # path = 'dataset/SAD_backup/behavior/'
# # target_folder = 'dataset/SAD/behavior/Diagram/'
#
# candidate_list = generate_canaidates()

def convert_mmd2png(source, target):
    # Run Mermaid CLI to convert
    subprocess.run(["mmdc", "-i", source, "-o", target, "-s", "3"], check=True)


# 1. generate PNG for behavior diagrams
def generate_png_behavior():
    path = 'dataset/SAD_backup/behavior/'
    target_file_path = 'dataset/SAD/behavior/Diagram/'
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith('.svg'):
            source_file_path = path + file
            svg2png(source_file_path, target_file_path + file.replace('.svg', '.png'))

# 2. generate PNG for structural diagrams
def generate_png_structural():
    # path1 = base_path + 'dataset/SAD_backup/structural/classDiagram/'
    path2 = base_path + 'dataset/SAD_backup/structural/classDiagram2/'
    target_path = base_path + 'dataset/SAD/structural/Diagram/'

    # file_list = os.listdir(path1)
    # for file in file_list:
    #     if file.endswith('.pdf'):
    #         source_file_path = path1 + file
    #         target_file_path = target_path + file.replace('.pdf', '.png')
    #         pdf2png(source_file_path, target_file_path)

    file_list = os.listdir(path2)
    for file in file_list:
        if file.endswith('.mmd'):
            print(file)
            source_file_path = path2 + file
            target_file_path = target_path + file.replace('.mmd', '.png')
            convert_mmd2png(source_file_path, target_file_path)

# 3. generate PNG for ER diagrams
def generate_png_ER():
    path = base_path + 'dataset/SAD_backup/ER/'
    target_path = base_path + 'dataset/SAD/ER/Diagram/'

    # file_list = os.listdir(path)
    # for file in file_list:
    #     if file.endswith('.json'):
    #         with open(path + file, 'r') as f:
    #             text = f.read()
    #         if 'numeric' in text:
    #             print(file)


    # # generate .mmd file
    file_list = os.listdir(path)
    for file in file_list:
        # file = 'ER_diagram_18.json'
        if file.endswith('.json') and '42' in file:
            source_file_path = path + file
            json_object = json.load(open(source_file_path, 'r'))
            mmd_script = json_to_mermaid(json_object)
            # mmd_script_list.append(mmd_script)
            with open(source_file_path.replace('.json', '.mmd'), 'w') as f:
                f.write(mmd_script)


    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith('.mmd') and '42' in file:
            print(file)
            source_file_path = path + file
            target_file_path = target_path + file.replace('.mmd', '.png')
            convert_mmd2png(source_file_path, target_file_path)


# a = {}
# for x in candidate_list:
#     if 'ER' in x:
#         with open(x, 'r') as f:
#             json_object = json.load(f)
#         mermaid_text = json_to_mermaid(json_object)
#         a[x] = mermaid_text
#     if 'structural' in x and ('UC.json' in x or 'US.json' in x):
#         file_name = x.split('/')[-1]
#         file_name = file_name.replace('.json', '.pdf')
#         pdf2png(path + file_name, target_folder + file_name.replace('.pdf', '.png'))
#
#         # file_name = file_name.replace('.json', '.svg')
#         # svg2png(path + file_name, target_folder + file_name.replace('.svg', '.png'))
