import json
import re


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

res_list = []
target_res_list = []

with open('experiment_result/all_1120.log', 'r') as f:
    for line in f.readlines():
        res_list.append(json.loads(line))

# question_type = 'counting'
question_type = 'retrieval'
# question_type = 'all'

if question_type == 'counting':
    target_question_types = [
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
elif question_type == 'retrieval':
    target_question_types = [
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

else:
    target_question_types = []

for res in res_list:
    if res['metadata']['sub_type'] in target_question_types:
        target_res_list.append(res)

classification = {
    'format_wrong': [],
    'json_wrong': [],
    'data_type_error': [],
    'correct': []
}

for i, res in enumerate(res_list):
    if target_question_types == [] or res['metadata']['sub_type'] in target_question_types:
        json_str = ''
        response = res['response']
        response = over_length_fix(response) # format error fix
        match = re.search(r'\[start\](.*?)\[end\]', response, flags=re.S)
        if match:
            json_str = match.group(1).strip()   # remove whitespace
        else:
            classification['format_wrong'].append(i)
            continue

        json_str = json_str_fix(json_str)
        try:
            obj = json.loads(json_str)
        except:
            classification['json_wrong'].append(i)
            continue

        if question_type == 'counting':
            if 'answer' in obj and isinstance(obj['answer'], int):
                classification['correct'].append(i)
            else:
                classification['data_type_error'].append(i)
        else:
            classification['correct'].append(i)




# still_json_error_list = []

# for i in classification['json_wrong']:
#     response = res_list[i]['response']
#     # Fix 1  }] -> ]}
#     if response.endswith('}]'):
#         response = response.replace('}]', ']}')
#     # Fix 2
#     if '"x1", "x2", ...' in response:
#         response = response.replace('"x1", "x2", ...', '')
#     # Fix 3
#     if '"x2", ...' in response:
#         response = response.replace('"x2", ...', '')
#     # Fix 4
#     if ', ...' in response:
#         response = response.replace(', ...', '')



# def format_error_analysis()
# error_analysis = {
#     '[start] issue': [],
#     '[end] issue': []
# }
# for i in classification['format_wrong']:
#     if '[start]' not in res_list[i]['response']:
#         error_analysis['[start] issue'].append(i)
#     elif '[end]' not in res_list[i]['response']:
#         error_analysis['[end] issue'].append(i)



# for i in classification['json_wrong']:
#     print(i)
#     print('Answer: ', res_list[i]['answer'])
#     response = over_length_fix(res_list[i]['response'])
#     match = re.search(r'\[start\](.*?)\[end\]', response, flags=re.S)
#     json_str = match.group(1).strip()
#     print('JSON STR: ', json_str)
#     print('"x2", ...' in json_str)
#     json_str = json_str.replace('"x2", ...', '')
#     print(json_str)
#     # print('Response: ', res_list[i]['response'])
#     # print('End of response: ', res_list[i]['response'][-40:])
#     a = input()


# problem type statistic

# statistic_dic = {}
#
# for i in classification['json_wrong']:
#     question_type = res_list[i]['metadata']['sub_type']
#     if question_type not in statistic_dic:
#         statistic_dic[question_type] = []
#
#     statistic_dic[question_type].append(i)
#
# for key in statistic_dic:
#     print(key, len(statistic_dic[key]))




###### format wrong distribution

# two_entities_in_the_same_cluster 938
# cluster_has_most_entities 15
# certain_cluster_contains_entity 67
# label_on_the_relation 8
# label_on_the_relation_target 122
# label_on_the_relation_source 66
# cluster_contains_certain_entity 64
# relation_target 3511
# which_relation_has_certain_label 231
# relation_statement 725
# relation_source 443
# type_on_the_relation 117
# entity_contains_certain_attribute 436
# entity_contains_certain_method 231

###### json wrong distribution

# label_on_the_relation_target 185
# label_on_the_relation_source 297
# type_on_the_relation 301
# two_entities_in_the_same_cluster 192
# relation_target 218
# relation_statement 331
# relation_source 141
# cluster_has_most_entities 6
# cluster_contains_certain_entity 31
# certain_cluster_contains_entity 24
# label_on_the_relation 5
# entity_contains_certain_attribute 1
# entity_contains_certain_method 2
# which_relation_has_certain_label 21


###### correct

# two_entities_in_the_same_cluster 715
# relation_statement 587
# certain_cluster_contains_entity 48
# label_on_the_relation 618
# label_on_the_relation_source 268
# label_on_the_relation_target 324
# cluster_contains_certain_entity 172
# type_on_the_relation 1447
# which_relation_has_certain_label 371
# relation_target 428
# relation_source 590
# cluster_has_most_entities 9
# entity_contains_certain_attribute 191
# entity_contains_certain_method 87
