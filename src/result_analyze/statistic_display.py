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
