import os
import json
import base64
from pathlib import Path

def build_prompt(question):
    instruction_prompt = (
        'Please answer the question strictly based on the given diagram and follow ALL rules below.\n'
        'Definitions:\n'
        '1. Entity: An individual, identifiable component in the diagram, represented by a distinct icon or label with text.\n'
        '2. Cluster: A visual container or boundary (circle, box, or similar shape) that encloses multiple related entities to indicate environment, region, or service domain.\n'
        '3. Relation: Any directional, bidirectional, or non-directional interaction between entities shown in the diagram.\n'
        '4. Relation label: The exact string attached to the relation arrow or line.\n'
        '5. Attribute: A descriptive element attached to an entity in the diagram, shown as text inside or near the entity, representing properties, configurations, or characteristics of that entity.\n'
        '6. Method: An operational element associated with an entity in the diagram, shown as a named action, capability, or functional label that indicates what behavior the entity performs or exposes.\n\n'
        'Answering Rules:\n'
        '1. Count all visible items shown inside the diagram. \n'
        '2. Name matching is case sensitive.\n'
        '3. Do NOT include explanations, reasoning, or text outside the JSON object.\n'
        '4. Output MUST follow the exact format shown below, including the [start] and [end] markers, the key name "answer", array brackets, and quotes around every string.\n'
        '5. Do NOT add extra fields, extra text, or comments.\n'
        '6. The JSON array MUST contain only the final answer values (e.g., entity names, cluster names, relation labels, counts, etc., depending on the question).'
        '\n\n')

    return instruction_prompt + question

def build_prompt_without_definition(question):
    instruction_prompt = (
        'Please answer the question strictly based on the given diagram and follow ALL rules below.\n'
        'Answering Rules:\n'
        '1. Count all visible items shown inside the diagram. \n'
        '2. Name matching is case sensitive.\n'
        '3. Do NOT include explanations, reasoning, or text outside the JSON object.\n'
        '4. Output MUST follow the exact format shown below, including the [start] and [end] markers, the key name "answer", array brackets, and quotes around every string.\n'
        '5. Do NOT add extra fields, extra text, or comments.\n'
        '6. The JSON array MUST contain only the final answer values (e.g., entity names, cluster names, relation labels, counts, etc., depending on the question).'
        '\n\n')

    return instruction_prompt + question


def build_prompt_without_rules(question):
    instruction_prompt = (
        'Please answer the question strictly based on the given diagram and follow ALL rules below.\n'
        'Definitions:\n'
        '1. Entity: An individual, identifiable component in the diagram, represented by a distinct icon or label with text.\n'
        '2. Cluster: A visual container or boundary (circle, box, or similar shape) that encloses multiple related entities to indicate environment, region, or service domain.\n'
        '3. Relation: Any directional, bidirectional, or non-directional interaction between entities shown in the diagram.\n'
        '4. Relation label: The exact string attached to the relation arrow or line.\n'
        '5. Attribute: A descriptive element attached to an entity in the diagram, shown as text inside or near the entity, representing properties, configurations, or characteristics of that entity.\n'
        '6. Method: An operational element associated with an entity in the diagram, shown as a named action, capability, or functional label that indicates what behavior the entity performs or exposes.\n\n'
        '\n\n')

    return instruction_prompt + question

def build_prompt_only_question(question):
    question_lines = question.split('\n')
    question_final = ''
    for line in question_lines:
        if line == 'Required Output Format (strict).':
            break
        else:
            question_final += line + '\n'
    return question_final.strip()