import json
import re
from collections import defaultdict
import os
import asyncio
import mimetypes
from openai import OpenAI, AsyncOpenAI
import matplotlib.pyplot as plt
import numpy as np


base_path = '../../'


def build_classification_prompt(response, answer):
    prompt = ('You are a strict evaluator. You will be given two inputs:\n'
              '1. answer: a list of strings (the ground truth)\n'
              '2. response: a list of strings (the model output)\n\n'
              'Your job is to classify how the response differs from the answer. Output exactly ONE label from the following set (no extra text):\n'
              '1. incorrect text\n'
              '2. response has more elements\n'
              '3. response has less elements\n'
              '4. all wrong elements\n'
              '5. partially correct\n\n'
              'Matching rules:\n'
              '1. Compare elements by exact string equality after trimming leading/trailing whitespace.\n'
              '2. Do not use synonyms, stemming, or semantic similarity.\n'
              '3. Treat matching as case-sensitive (e.g., "Apple" != "apple").\n'
              '4. IMPORTANT: Lists may contain duplicates. Therefore, all containment/overlap checks must be done using MULTISET (bag) logic, not set logic.\n\n'
              'Multiset definitions:\n'
              '1. Let count_A(x) be the number of times string x appears in answer.\n'
              '2. Let count_R(x) be the number of times string x appears in response.\n'
              '3. Multiset overlap count for x is min(count_A(x), count_R(x)).\n'
              '4. Total overlap = sum over all x of min(count_A(x), count_R(x)).\n'
              '5. “A is contained in R” (A ⊆ R in multiset sense) means: for every string x, count_A(x) <= count_R(x).\n'
              '6. “R is contained in A” means: for every string x, count_R(x) <= count_A(x).\n\n'
              'Decision procedure (apply in this exact order):\n'
              '1. Compute total_overlap as the sum of min(count_A(x), count_R(x)) over all strings x.\n'
              '2. If total_overlap == 0, output: "all wrong elements"\n'
              '3. Else if (for every x, count_A(x) <= count_R(x)) AND there exists some x with count_R(x) > count_A(x), output: response has more elements\n'
              '4. Else if (for every x, count_R(x) <= count_A(x)) AND there exists some x with count_A(x) > count_R(x), output: response has less elements\n'
              '5. Else if len(response) == len(answer) AND total_overlap == len(answer) BUT response is not exactly identical to answer as a list (i.e., same multiset of elements but at least one element differs in spelling/typo/character-level so it cannot match exactly), output: incorrect text\n'
              '6. Else output: partially correct\n\n'
              'Inputs:\n'
              'response: %s\n'
              'answer: %s\n\n'
              'Return only the label.') % (response, answer)

    return prompt

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
        'certain_cluster_contains_entity',
        'label_on_the_relation',
        'label_on_the_relation_source',
        'label_on_the_relation_target',
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

def load_sub_types():
    sub_types = [
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

        'cluster_has_most_entities',
        'relation_statement',
        'certain_cluster_contains_entity',
        'label_on_the_relation',
        'label_on_the_relation_source',
        'label_on_the_relation_target',
        'cluster_contains_certain_entity',
        'entity_contains_certain_attribute',
        'entity_contains_certain_method',
        'type_on_the_relation',
        'relation_source',
        'relation_target',
        'which_relation_has_certain_label'
    ]

    return sub_types

def deduplication(json_list):
    seen = set()
    result = []

    for obj in json_list:
        # Convert the selected keys into a hashable tuple
        key = (
            obj.get("diagram_type"),
            obj.get("file"),
            obj.get("question"),
            json.dumps(obj.get("answer"), sort_keys=True),
            json.dumps(obj.get("metadata"), sort_keys=True),
        )

        if key not in seen:
            seen.add(key)
            result.append(obj)

    return result

def generate_statistic_dic(file):
    QA_response_list = []
    with open(base_path + 'experiment_result/response_result/%s' % (file), 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            QA_response_list.append(content)
            # print(content['response'])

    for i, QA_response in enumerate(QA_response_list):
        # if QA_response['file'] in special_file_list:
        response_final = response_processing(QA_response['response'])
        # response_final = QA_response['response']
        try:
            response = json.loads(response_final)['answer']
        except:
            # print(i, 'ERROR')
            QA_response['evaluation_result'] = 'Parse Error'
            continue
        answer = QA_response['answer']
        # print(i, response, answer)
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'counting':
            if response == answer[0]:
                QA_response['evaluation_result'] = 'True'
            else:
                QA_response['evaluation_result'] = 'False'
        # retrieval problem
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'retrieval':
            if sorted(response) == sorted(answer):
                QA_response['evaluation_result'] = 'True'
            else:
                QA_response['evaluation_result'] = 'False'

    statistic_dict = {
        'behavior': {},
        'structural': {},
        'ER': {},
        'all': {}
    }

    sub_types = load_sub_types()
    for x in sub_types:
        for key in statistic_dict:
            statistic_dict[key][x] = []

    for QA_response in QA_response_list:
        statistic_dict[QA_response['diagram_type']][QA_response["metadata"]['sub_type']].append(
            QA_response['evaluation_result'])
        statistic_dict['all'][QA_response["metadata"]['sub_type']].append(QA_response['evaluation_result'])

    return statistic_dict

def generate_statistic_dic_all(file):
    QA_response_list = []
    with open(base_path + 'experiment_result/response_result/%s' % (file), 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            QA_response_list.append(content)
            # print(content['response'])

    for i, QA_response in enumerate(QA_response_list):
        # if QA_response['file'] in special_file_list:
        response_final = response_processing(QA_response['response'])
        # response_final = QA_response['response']
        try:
            response = json.loads(response_final)['answer']
        except:
            # print(i, 'ERROR')
            QA_response['evaluation_result'] = 'Parse Error'
            continue
        answer = QA_response['answer']
        # print(i, response, answer)
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'counting':
            if response == answer[0]:
                QA_response['evaluation_result'] = 'True'
            else:
                QA_response['evaluation_result'] = 'False'
        # retrieval problem
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'retrieval':
            if QA_response['metadata']['sub_type'] in ['type_on_the_relation'] and QA_response['diagram_type'] == 'ER':
                if response == answer[0]:
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'

            elif QA_response['metadata']['sub_type'] in ['entity_contains_certain_method']:
                response = [x.replace('()', '') for x in response]
                if sorted(response) == sorted(answer):
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'
            elif QA_response['metadata']['sub_type'] in ['which_relation_has_certain_label']:
                try:
                    if isinstance(response, list) and len(response) > 0:
                        response = response[0]
                    if isinstance(response, str) and '[' in response and ']' in response:
                        response = eval(response)
                except:
                    QA_response['evaluation_result'] = 'Parse Error'
                    continue
                    # response = [x[0].replace('()', '') for x in response]
                if response == answer[0]:
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'
            else:
                if sorted(response) == sorted(answer):
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'

    statistic_dict = {
        'behavior': {},
        'structural': {},
        'ER': {},
        'all': {}
    }

    sub_types = load_sub_types()
    for x in sub_types:
        for key in statistic_dict:
            statistic_dict[key][x] = []

    for QA_response in QA_response_list:
        statistic_dict[QA_response['diagram_type']][QA_response["metadata"]['sub_type']].append(QA_response)
        statistic_dict['all'][QA_response["metadata"]['sub_type']].append(QA_response)

    return statistic_dict

def statistic_table(file):
    QA_response_list = []
    with open(base_path + 'experiment_result/response_result/%s' % (file), 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            QA_response_list.append(content)
            # print(content['response'])



    for i, QA_response in enumerate(QA_response_list):
        # print(i)
        # if QA_response['file'] in special_file_list:
        response_final = response_processing(QA_response['response'])
        # response_final = QA_response['response']
        try:
            response = json.loads(response_final)['answer']
        except:
            # print(i, 'ERROR')
            QA_response['evaluation_result'] = 'Parse Error'
            continue
        answer = QA_response['answer']
        # print(i, response, answer)
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'counting':
            if response == answer[0]:
                QA_response['evaluation_result'] = 'True'
            else:
                QA_response['evaluation_result'] = 'False'
        # retrieval problem
        if check_counting_or_retrieval(QA_response['metadata']['sub_type']) == 'retrieval':
            if QA_response['metadata']['sub_type'] in ['type_on_the_relation'] and QA_response['diagram_type'] == 'ER':
                if response == answer[0]:
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'

            elif QA_response['metadata']['sub_type'] in ['entity_contains_certain_method']:
                response = [x.replace('()', '') for x in response]
                if sorted(response) == sorted(answer):
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'
            elif QA_response['metadata']['sub_type'] in ['which_relation_has_certain_label']:
                try:
                    if isinstance(response, list) and len(response) > 0:
                        response = response[0]
                    if isinstance(response, str) and '[' in response and ']' in response:
                        response = eval(response)
                except:
                    QA_response['evaluation_result'] = 'Parse Error'
                    continue
                    # response = [x[0].replace('()', '') for x in response]
                if response == answer[0]:
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'
            else:
                if sorted(response) == sorted(answer):
                    QA_response['evaluation_result'] = 'True'
                else:
                    QA_response['evaluation_result'] = 'False'



    statistic_dict = {
        'behavior': {},
        'structural': {},
        'ER': {},
        'all': {}
    }

    sub_types = load_sub_types()
    for x in sub_types:
        for key in statistic_dict:
            statistic_dict[key][x] = []

    for QA_response in QA_response_list:
        statistic_dict[QA_response['diagram_type']][QA_response["metadata"]['sub_type']].append(QA_response['evaluation_result'])
        statistic_dict['all'][QA_response["metadata"]['sub_type']].append(QA_response['evaluation_result'])

    return statistic_dict
