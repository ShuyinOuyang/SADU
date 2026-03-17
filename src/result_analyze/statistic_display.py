import json
import re
import numpy as np
import os


# show max/mean/min No. entity / No. relation

base_path = '../../'

def generate_message_qa_list(diagram_type):
    json_object_list = []
    if diagram_type == "all":
        diagram_type_list = ["behavior", "structural", "ER"]
        for diagram_type in diagram_type_list:
            json_object_path = base_path + 'dataset/SAD/' + diagram_type + '/json_object/'
            qa_path = base_path + 'dataset/SAD/' + diagram_type + '/QA/'
            for file in os.listdir(json_object_path):
                with open(os.path.join(json_object_path, file), "r") as f:
                    json_object = json.load(f)
                with open(os.path.join(qa_path, file.replace('.json', '_QA.json')), "r") as f:
                    qa_object = json.load(f)
                json_object['QA'] = qa_object
                json_object_list.append(json_object)
    else:
        qa_path = base_path + 'dataset/SAD/' + diagram_type + '/QA/'
        # img_path = base_path + 'dataset/SAD/' + diagram_type + '/Diagram/'
        json_object_path = base_path + 'dataset/SAD/' + diagram_type + '/json_object/'

        for file in os.listdir(json_object_path):
            # print(file)
            with open(os.path.join(json_object_path, file), "r") as f:
                json_object = json.load(f)
            with open(os.path.join(qa_path, file.replace('.json', '_QA.json')), "r") as f:
                qa_object = json.load(f)
            json_object['QA'] = qa_object
            # print(json_object.keys())
            json_object_list.append(json_object)

    return json_object_list

# file_list = {
#     '512/gemini-2.5-flash-lite_response_0223_t_0.log': 'gemini-2.5-flash-lite',
#     '512/gemini-2.5-flash_response_0223_t_0.log': 'gemini-2.5-flash',
#     '512/gemini-3.1-flash-lite-preview_response_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
#     '512/gemini-3-flash-preview_response_0223_t_0.log': 'gemini-3-flash-preview',
#
#     '512/claude-haiku-4-5_response_0223_t_0.log': 'claude-haiku-4.5',
#     '512/claude-sonnet-4-5_response_0223_t_0.log': 'claude-sonnet-4.5',
#
#     '512/gpt-5-nano_response_0223_t_1.log': 'gpt-5-nano',
#     '512/gpt-4o-mini_response_0223_t_0.log': 'gpt-4o-mini',
#
#     '512/qwen_2.5-VL-32B_response_0223_t_0.log': 'qwen-2.5-VL-32B',
#     '512/qwen_2.5-VL-7B_response_0223_t_0.log': 'qwen-2.5-VL-7B',
#     '512/qwen_2.5-VL-3B_response_0223_t_0.log': 'qwen-2.5-VL-3B'
# }


    # behavior_acc = return_accuray(x, 'behavior')
    # structural_acc = return_accuray(x, 'structural')
    # ER_acc = return_accuray(x, 'ER')
    # all_acc = return_accuray(x, 'all')
    #
    # print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' % (
    #     RQ1_file_list[x], behavior_acc, structural_acc, ER_acc, all_acc
    # ))

diagram_type_list = ["behavior", "structural", "ER", "all"]
for diagram_type in diagram_type_list:
    json_object_list = generate_message_qa_list(diagram_type)
    No_of_diagram = len(json_object_list)
    mean_entity_number = np.mean([len(x['entity']) for x in json_object_list])
    max_entity_number = np.max([len(x['entity']) for x in json_object_list])
    min_entity_number = np.min([len(x['entity']) for x in json_object_list])

    mean_relation_number = np.mean([len(x['relation']) for x in json_object_list])
    max_relation_number = np.max([len(x['relation']) for x in json_object_list])
    min_relation_number = np.min([len(x['relation']) for x in json_object_list])

    mean_cluster_number = np.mean([len(x['cluster']) for x in json_object_list])
    max_cluster_number = np.max([len(x['cluster']) for x in json_object_list])
    min_cluster_number = np.min([len(x['cluster']) for x in json_object_list])

    # QA
    QA_subtype = []
    for x in json_object_list:
        for y in x['QA']:
            QA_subtype.append(y['metadata']['sub_type'])
    No_of_QA_subtype = len(set(QA_subtype))
    No_of_QA_pairs = sum([len(x['QA']) for x in json_object_list])

    print('%s & %s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %s & %s \\\\' % (
        diagram_type, No_of_diagram, max_entity_number, min_entity_number, mean_entity_number,
        max_relation_number, min_relation_number, mean_relation_number,
        No_of_QA_pairs, No_of_QA_subtype))
    # print('%.2f & %.2f & %.2f' % (mean_relation_number, max_relation_number, min_relation_number))
    # print('%.2f & %.2f & %.2f' % (mean_cluster_number, max_cluster_number, min_cluster_number))
    # print('----')