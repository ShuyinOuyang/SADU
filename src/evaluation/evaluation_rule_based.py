import json
import re
import numpy as np

base_path = '../../'

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
        'two_entities_in_the_same_cluster',
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
        # 'two_entities_in_the_same_cluster',
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

def get_statistic_table(file):
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



    return QA_response_list

def statistic_table(file, diagram_type, only_total=True):
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


    for QA_sub_type in statistic_dict[diagram_type]:
        if statistic_dict[diagram_type][QA_sub_type] == []:
            print(QA_sub_type)
        else:
            true_rate = statistic_dict[diagram_type][QA_sub_type].count('True') / len(
                statistic_dict[diagram_type][QA_sub_type])
            false_rate = statistic_dict[diagram_type][QA_sub_type].count('False') / len(
                statistic_dict[diagram_type][QA_sub_type])
            parse_error_rate = statistic_dict[diagram_type][QA_sub_type].count('Parse Error') / len(
                statistic_dict[diagram_type][QA_sub_type])

            if only_total == False:
                print('%s & %.2f\%% & %.2f\%% \\\\' %
                      (QA_sub_type.replace('_', ' '),
                       # len(statistic_dict[diagram_type][QA_sub_type]),
                       # statistic_dict[diagram_type][QA_sub_type].count('True'),
                       true_rate * 100,
                       # statistic_dict[diagram_type][QA_sub_type].count('False'),
                       # false_rate * 100,
                       # statistic_dict[diagram_type][QA_sub_type].count('Parse Error'),
                       parse_error_rate * 100
                       ))

    sum_total = sum([len(statistic_dict[diagram_type][QA_sub_type]) for QA_sub_type in statistic_dict[diagram_type]])
    sum_true = sum([statistic_dict[diagram_type][QA_sub_type].count('True') for QA_sub_type in statistic_dict[diagram_type]])
    sum_false = sum([statistic_dict[diagram_type][QA_sub_type].count('False') for QA_sub_type in statistic_dict[diagram_type]])
    sum_error = sum([statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type]])
    sum_true_counting = sum([statistic_dict[diagram_type][QA_sub_type].count('True') for QA_sub_type in statistic_dict[diagram_type] if check_counting_or_retrieval(QA_sub_type) == 'counting'])
    sum_true_retrieval = sum([statistic_dict[diagram_type][QA_sub_type].count('True') for QA_sub_type in statistic_dict[diagram_type] if check_counting_or_retrieval(QA_sub_type) == 'retrieval'])
    sum_error_counting = sum(
        [statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type] if
         check_counting_or_retrieval(QA_sub_type) == 'counting'])
    sum_error_retrieval = sum(
        [statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type] if
         check_counting_or_retrieval(QA_sub_type) == 'retrieval'])
    sum_total_counting = sum([len(statistic_dict[diagram_type][QA_sub_type]) for QA_sub_type in statistic_dict[diagram_type] if check_counting_or_retrieval(QA_sub_type) == 'counting'])
    sum_total_retrieval = sum([len(statistic_dict[diagram_type][QA_sub_type]) for QA_sub_type in statistic_dict[diagram_type] if check_counting_or_retrieval(QA_sub_type) == 'retrieval'])

    if only_total:
        print('%s\t%s\t%s\t%.2f%%\t%s\t%.2f%%\t%s\t%.2f%%' %
              (file,
               sum_total,
               sum_true,
               sum_true/sum_total * 100,
               sum_false,
               sum_false/sum_total  * 100,
               sum_error,
               sum_error/sum_total  * 100
               ))
    else:
        print('%s & %.2f\%% & %.2f\%% \\\\' %
              ("Total Counting",
               # sum_total,
               # sum_true,
               sum_true_counting / sum_total_counting * 100,
               # sum_false,
               # sum_false/sum_total  * 100,
               # sum_error,
               sum_error_counting / sum_total_counting * 100
               ))
        print('%s & %.2f\%% & %.2f\%% \\\\' %
              ("Total Retrieval",
               # sum_total,
               # sum_true,
               sum_true_retrieval/sum_total_retrieval * 100,
               # sum_false,
               # sum_false/sum_total  * 100,
               # sum_error,
               sum_error_retrieval/sum_total_retrieval  * 100
               ))
        print('%s & %.2f\%% & %.2f\%% \\\\' %
              ("Total",
               # sum_total,
               # sum_true,
               sum_true/sum_total * 100,
               # sum_false,
               # sum_false/sum_total  * 100,
               # sum_error,
               sum_error/sum_total  * 100
               ))
    return QA_response_list

def return_accuray(file, diagram_type):
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


    for QA_sub_type in statistic_dict[diagram_type]:
        if statistic_dict[diagram_type][QA_sub_type] == []:
            # print(QA_sub_type)
            pass
        else:
            true_rate = statistic_dict[diagram_type][QA_sub_type].count('True') / len(
                statistic_dict[diagram_type][QA_sub_type])
            false_rate = statistic_dict[diagram_type][QA_sub_type].count('False') / len(
                statistic_dict[diagram_type][QA_sub_type])
            parse_error_rate = statistic_dict[diagram_type][QA_sub_type].count('Parse Error') / len(
                statistic_dict[diagram_type][QA_sub_type])


    sum_total = sum([len(statistic_dict[diagram_type][QA_sub_type]) for QA_sub_type in statistic_dict[diagram_type]])
    sum_true = sum([statistic_dict[diagram_type][QA_sub_type].count('True') for QA_sub_type in statistic_dict[diagram_type]])
    # sum_false = sum([statistic_dict[diagram_type][QA_sub_type].count('False') for QA_sub_type in statistic_dict[diagram_type]])
    # sum_error = sum([statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type]])
    return sum_true/sum_total * 100


def RQ1():
    diagram_type_list = ["behavior", "structural", "ER", "all"]
    diagram_type = diagram_type_list[3]
    file = '512/gemini-2.5-flash_response_0223_t_0.log'
    # file = 'hard_claude-haiku-4-5_response_0223_t_0.log'
    # file = 'hard_gpt-4o-mini_response_0223_t_0.log'
    # file = 'hard_qwen_2.5-VL-7B_response_0223_t_0.log'


    # RQ3: Prompt
    RQ3_file_list = {
        'different_prompt/gemini-2.5-flash-lite_response_0223_t_0.log': 'full & gemini-2.5-flash-lite',
        'different_prompt/gemini-2.5-flash_response_0223_t_0.log': 'full & gemini-2.5-flash',
        'different_prompt/gemini-3.1-flash-lite-preview_response_0223_t_0.log': 'full & gemini-3.1-flash-lite-preview',
        'different_prompt/gemini-3-flash-preview_response_0223_t_0.log': 'full & gemini-3-flash-preview',

        'different_prompt/without_definition_gemini-2.5-flash-lite_response_0306_t_0.log': 'without definition & gemini-2.5-flash-lite',
        'different_prompt/without_definition_gemini-2.5-flash_response_0306_t_0.log': 'without definition & gemini-2.5-flash',
        'different_prompt/without_definition_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'without definition & gemini-3.1-flash-lite-preview',
        'different_prompt/without_definition_gemini-3-flash-preview_response_0306_t_0.log': 'without definition & gemini-3-flash-preview',

        'different_prompt/without_rules_gemini-2.5-flash-lite_response_0306_t_0.log': 'without rules & gemini-2.5-flash-lite',
        'different_prompt/without_rules_gemini-2.5-flash_response_0306_t_0.log': 'without rules & gemini-2.5-flash',
        'different_prompt/without_rules_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'without rules & gemini-3.1-flash-lite-preview',
        'different_prompt/without_rules_gemini-3-flash-preview_response_0306_t_0.log': 'without rules & gemini-3-flash-preview',

        'different_prompt/only_question_gemini-2.5-flash-lite_response_0306_t_0.log': 'only question & gemini-2.5-flash-lite',
        'different_prompt/only_question_gemini-2.5-flash_response_0306_t_0.log': 'only question & gemini-2.5-flash',
        'different_prompt/only_question_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'only question & gemini-3.1-flash-lite-preview',
        'different_prompt/only_question_gemini-3-flash-preview_response_0306_t_0.log': 'only question & gemini-3-flash-preview',
    }


    RQ1_file_list = {
        '512/gemini-2.5-flash-lite_response_0223_t_0.log': 'gemini-2.5-flash-lite',
        '512/gemini-2.5-flash_response_0223_t_0.log': 'gemini-2.5-flash',
        '512/gemini-3.1-flash-lite-preview_response_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
        '512/gemini-3-flash-preview_response_0223_t_0.log': 'gemini-3-flash-preview',

        '512/claude-haiku-4-5_response_0223_t_0.log': 'claude-haiku-4.5',
        '512/claude-sonnet-4-5_response_0223_t_0.log': 'claude-sonnet-4.5',

        '512/gpt-5-nano_response_0223_t_1.log': 'gpt-5-nano',
        '512/gpt-4o-mini_response_0223_t_0.log': 'gpt-4o-mini',

        '512/qwen_2.5-VL-32B_response_0223_t_0.log': 'qwen-2.5-VL-32B',
        '512/qwen_2.5-VL-7B_response_0223_t_0.log': 'qwen-2.5-VL-7B',
        '512/qwen_2.5-VL-3B_response_0223_t_0.log': 'qwen-2.5-VL-3B'
    }

    for x in RQ1_file_list:
        behavior_acc = return_accuray(x, 'behavior')
        structural_acc = return_accuray(x, 'structural')
        ER_acc = return_accuray(x, 'ER')
        all_acc = return_accuray(x, 'all')

        print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' % (
            RQ1_file_list[x], behavior_acc, structural_acc, ER_acc, all_acc
        ))


def RQ3():
    diagram_type_list = ["behavior", "structural", "ER", "all"]
    diagram_type = diagram_type_list[3]
    file = '512/gemini-2.5-flash_response_0223_t_0.log'
    # file = 'hard_claude-haiku-4-5_response_0223_t_0.log'
    # file = 'hard_gpt-4o-mini_response_0223_t_0.log'
    # file = 'hard_qwen_2.5-VL-7B_response_0223_t_0.log'

    # RQ3: Prompt
    RQ3_file_list = {
        'different_prompt/gemini-2.5-flash-lite_response_0223_t_0.log': 'full & gemini-2.5-flash-lite',
        'different_prompt/gemini-2.5-flash_response_0223_t_0.log': 'full & gemini-2.5-flash',
        'different_prompt/gemini-3.1-flash-lite-preview_response_0223_t_0.log': 'full & gemini-3.1-flash-lite-preview',
        'different_prompt/gemini-3-flash-preview_response_0223_t_0.log': 'full & gemini-3-flash-preview',

        'different_prompt/without_definition_gemini-2.5-flash-lite_response_0306_t_0.log': 'without definition & gemini-2.5-flash-lite',
        'different_prompt/without_definition_gemini-2.5-flash_response_0306_t_0.log': 'without definition & gemini-2.5-flash',
        'different_prompt/without_definition_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'without definition & gemini-3.1-flash-lite-preview',
        'different_prompt/without_definition_gemini-3-flash-preview_response_0306_t_0.log': 'without definition & gemini-3-flash-preview',

        'different_prompt/without_rules_gemini-2.5-flash-lite_response_0306_t_0.log': 'without rules & gemini-2.5-flash-lite',
        'different_prompt/without_rules_gemini-2.5-flash_response_0306_t_0.log': 'without rules & gemini-2.5-flash',
        'different_prompt/without_rules_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'without rules & gemini-3.1-flash-lite-preview',
        'different_prompt/without_rules_gemini-3-flash-preview_response_0306_t_0.log': 'without rules & gemini-3-flash-preview',

        'different_prompt/only_question_gemini-2.5-flash-lite_response_0306_t_0.log': 'only question & gemini-2.5-flash-lite',
        'different_prompt/only_question_gemini-2.5-flash_response_0306_t_0.log': 'only question & gemini-2.5-flash',
        'different_prompt/only_question_gemini-3.1-flash-lite-preview_response_0306_t_0.log': 'only question & gemini-3.1-flash-lite-preview',
        'different_prompt/only_question_gemini-3-flash-preview_response_0306_t_0.log': 'only question & gemini-3-flash-preview',
    }

    for x in RQ3_file_list:
        behavior_acc = return_accuray(x, 'behavior')
        structural_acc = return_accuray(x, 'structural')
        ER_acc = return_accuray(x, 'ER')
        all_acc = return_accuray(x, 'all')

        print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' % (
            RQ3_file_list[x], behavior_acc, structural_acc, ER_acc, all_acc
        ))


def hard_evaluation():
    diagram_type_list = ["behavior", "structural", "ER", "all"]
    diagram_type = diagram_type_list[3]
    # file = '512/gemini-2.5-flash_response_0223_t_0.log'
    # # file = 'hard_claude-haiku-4-5_response_0223_t_0.log'
    # # file = 'hard_gpt-4o-mini_response_0223_t_0.log'
    # # file = 'hard_qwen_2.5-VL-7B_response_0223_t_0.log'
    file_list = {
        'sythesis/hard_gemini-2.5-flash-lite_response_0223_t_0.log': 'gemini-2.5-flash-lite',
        'sythesis/hard_gemini-2.5-flash_response_0223_t_0.log': 'gemini-2.5-flash',
        'sythesis/hard_gemini-3.1-flash-lite-preview_response_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
        'sythesis/hard_gemini-3-flash-preview_response_0223_t_0.log': 'gemini-3-flash-preview',

        'sythesis/hard_claude-haiku-4-5_response_0223_t_0.log': 'claude-haiku-4.5',
        'sythesis/hard_claude-sonnet-4-5_response_0223_t_0.log': 'claude-sonnet-4.5',

        'sythesis/hard_gpt-4o-mini_response_0223_t_0.log': 'gpt-4o-mini',
        'sythesis/hard_gpt-5-nano_response_0223_t_1.log': 'gpt-5-nano',

        'sythesis/hard_qwen_2.5-VL-3B_response_0223_t_0.log': 'qwen-2.5-VL-3B',
        'sythesis/hard_qwen_2.5-VL-7B_response_0223_t_0.log': 'qwen-2.5-VL-7B',
        'sythesis/hard_qwen_2.5-VL-32B_response_0223_t_0.log': 'qwen-2.5-VL-32B'

    }
    for file in file_list:
        QA_response_list = get_statistic_table(file)
        # for hard only
        long_arrow = []
        multi_arrow = []
        not_right_arrow = []
        overlap_arrow = []
        for i, x in enumerate(QA_response_list):
            if i < 5:
                if x['evaluation_result'] == 'True':
                    long_arrow.append(1)
                else:
                    long_arrow.append(0)
            elif i < 10:
                if x['evaluation_result'] == 'True':
                    multi_arrow.append(1)
                else:
                    multi_arrow.append(0)
            elif i < 15:
                if x['evaluation_result'] == 'True':
                    not_right_arrow.append(1)
                else:
                    not_right_arrow.append(0)
            else:
                if x['evaluation_result'] == 'True':
                    overlap_arrow.append(1)
                else:
                    overlap_arrow.append(0)
        print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' % (
            file_list[file],
            np.mean(long_arrow) * 100,
            np.mean(multi_arrow) * 100,
            np.mean(not_right_arrow) * 100,
            np.mean(overlap_arrow) * 100
        ))


# diagram_type = 'all'
# file = '512/gemini-3-flash-preview_response_0223_t_0.log'
# statistic_table(file, diagram_type, False)

