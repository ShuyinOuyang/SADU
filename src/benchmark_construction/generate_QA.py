import json
import os
from generate_QA_util import *

counting_format_instruction = ('Required Output Format (strict).\n'
                               '[start]\n'
                               '{"answer": x}\n'
                               '[end]\n'
                               'The answer MUST be a valid JSON object.\n'
                               'x must be a number.\n')

retrieval_format_instruction = ('Required Output Format (strict).\n'
                                '[start]\n'
                                '{"answer": ["x1", "x2", ...]}\n'
                                '[end]\n'
                                'The answer MUST be a valid JSON object.'
                                'Replace "x1", "x2", ... with the actual answer strings.')

# counting_format_instruction_oneshot = ('The response should be a JSON object and strictly adhere to the following example output format, where x is a number.\n'
#                                '[start]\n'
#                                '{"answer": x}\n'
#                                '[end]\n')



# retrieval_format_instruction_oneshot = ('The response should be a JSON object and strictly adhere to the following example output format, '
#                                 'where x1, x2, ... should be one or more names of the retrieved object. '
#                                 'The answer should be case sensitive. \n'
#                                 '[start]\n'
#                                 '{"answer": ["x1", "x2", ...]}\n'
#                                 '[end]\n')

# How many entities are in the diagram (do not include the cluster)
def generate_total_entity_number(json_object):
    QA_list = []
    total_entity_num = len(json_object['entity'])
    answer = total_entity_num
    QA_ = {
        'question': 'How many entities are in the diagram?' + '\n' + counting_format_instruction,
        'answer': [answer],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'total_entity_number',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)

    return QA_list


# How many entities are in the diagram (do not include the cluster)
def generate_total_relation_number(json_object):
    QA_list = []
    total_relation_num = len(json_object['relation'])
    answer = total_relation_num
    QA_ = {
        'question': 'How many relations are in the diagram?' + '\n' + counting_format_instruction,
        'answer': [answer],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'total_relation_number',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)

    return QA_list


# How many entities have more than one relation?
def generate_entities_have_more_than_one_relations(json_object):
    QA_list = []
    # calculate entities with more than one relation
    ans = calculate_how_many_entities_have_more_than_one_relations(json_object)
    QA_ = {
        'question': 'How many entities have more than one relation?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'entities_have_more_than_one_relations',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many clusters are there?
def generate_total_cluster_number(json_object):
    QA_list = []
    total_cluster_num = len(json_object['cluster'])
    ans = total_cluster_num
    QA_ = {
        'question': 'How many clusters are in the diagram?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'total_cluster_number',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many entities are not contained in clusters?
def generate_how_many_entities_not_in_clusters(json_object):
    QA_list = []
    ans = calculate_how_many_entities_not_in_clusters(json_object)
    QA_ = {
        'question': 'How many entities are not contained in any cluster?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'how_many_entities_not_in_clusters',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many relations have labels on them?
def generate_how_many_relations_have_label(json_object):
    QA_list = []
    ans = calculate_how_many_relations_have_label(json_object)
    QA_ = {
        'question': 'How many relations have a label?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'how_many_relations_have_label',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many clusters have clusters within? _____
def generate_how_many_clusters_have_clusters_within(json_object):
    QA_list = []
    ans = calculate_how_many_clusters_have_clusters_within(json_object)
    QA_ = {
        'question': 'How many clusters contain at least one sub-cluster (nested clusters)?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'how_many_clusters_have_clusters_within',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many entities does Cluster A have?
def generate_how_many_entities_does_certain_cluster_have(json_object):
    QA_list = []
    entity_ans_pair_list = find_how_many_entities_does_certain_cluster_have(json_object)
    for entity_ans_pair in entity_ans_pair_list:
        ans = entity_ans_pair[2]
        cluster_name = entity_ans_pair[1]
        if cluster_name:
            QA_ = {
                    'question': 'How many entities are contained in Cluster \'%s\'?' % (cluster_name) + '\n' + counting_format_instruction,
                    'answer': [ans],
                    'metadata': {
                        'type': 'fill_in_the_blank',
                        'sub_type': 'how_many_entities_does_certain_cluster_have',
                        'difficulty': 'basic',
                    }
                }
            QA_list.append(QA_)

    return QA_list


# How many relation types are there?______
def generate_how_many_relation_types(json_object):
    QA_list = []
    ans = calculate_how_many_relation_types(json_object)
    QA_ = {
        'question': 'How many relation types appear in the diagram?' + '\n' + counting_format_instruction,
        'answer': [ans],
        'metadata': {
            'type': 'fill_in_the_blank',
            'sub_type': 'how_many_relation_types',
            'difficulty': 'basic',
        }
    }
    QA_list.append(QA_)
    return QA_list


# How many attributes Entity A has? _____
def generate_how_many_attributes_certain_entity_has(json_object):
    QA_list = []
    for entity in json_object['entity']:
        entity_name = json_object['entity'][entity]['name']
        if 'attribute' in json_object['entity'][entity]:
            total_number_attributes = len(json_object['entity'][entity]['attribute'])
            ans = total_number_attributes
            QA_ = {
                'question': 'How many attributes does Entity \'%s\' have?' % (entity_name) + '\n' + counting_format_instruction,
                'answer': [ans],
                'metadata': {
                    'type': 'fill_in_the_blank',
                    'sub_type': 'how_many_attributes_certain_entity_has',
                    'difficulty': 'intermediate',
                }
            }
            QA_list.append(QA_)
    return QA_list


# How many method Entity A has? _____
def generate_how_many_methods_certain_entity_has(json_object):
    QA_list = []
    for entity in json_object['entity']:
        entity_name = json_object['entity'][entity]['name']
        if 'method' in json_object['entity'][entity]:
            total_number_methods = len(json_object['entity'][entity]['method'])
            ans = total_number_methods
            QA_ = {
                'question': 'How many methods does Entity \'%s\' have?' % (entity_name) + '\n' + counting_format_instruction,
                'answer': [ans],
                'metadata': {
                    'type': 'fill_in_the_blank',
                    'sub_type': 'how_many_methods_certain_entity_has',
                    'difficulty': 'intermediate',
                }
            }
            QA_list.append(QA_)
    return QA_list

# =================================================================

# Which cluster has the most entities?
def generate_cluster_has_most_entities(json_object):
    QA_list = []
    ans_list, _ = find_which_cluster_has_the_most_clusters(json_object)
    ans_list = sorted(ans_list)
    if ans_list:
        QA_ = {
            'question': 'Which cluster(s) contain the most entities?' + '\n' + retrieval_format_instruction,
            'answer': ans_list,
            'metadata': {
                'type': 'fill_in_the_blank',
                'sub_type': 'cluster_has_most_entities',
                'difficulty': 'basic',
            }
        }
        QA_list.append(QA_)
    return QA_list

# Entity A has a relation with Entity ______
def generate_relation_statement(json_object):
    QA_list = []

    ans_pair_list = find_certain_entity_has_a_relation_with_others(json_object)
    for ans_pair in ans_pair_list:
        entity_name, ans_list, wrong_options_list = ans_pair
        ans_list = sorted(ans_list)
        QA_ = {
            'question': 'Which entity has a relation with Entity \'%s\'?' % (json_object['entity'][entity_name]['name']) + '\n' + retrieval_format_instruction,
            'answer': ans_list,
            'metadata': {
                'type': 'fill_in_the_blank',
                'sub_type': 'relation_statement',
                'difficulty': 'basic',
            }
        }
        QA_list.append(QA_)

    return QA_list

# Entity A and Entity _____ are in the same cluster.
def generate_two_entities_in_the_same_cluster(json_object):
    QA_list = []

    QA_pair = find_two_entities_in_the_same_cluster(json_object)

    for x in QA_pair:
        entity_name, ans_list = x
        ans_list = sorted(ans_list)
        QA_ = {
            'question': 'Which entities are in the same cluster as entity \'%s\'?' % (entity_name) + '\n' + retrieval_format_instruction,
            'answer': ans_list,
            'metadata': {
                'type': 'fill_in_the_blank',
                'sub_type': 'two_entities_in_the_same_cluster',
                'difficulty': 'basic',
            }
        }

        QA_list.append(QA_)

    return QA_list

# Cluster A contains Entity _____.
def generate_certain_cluster_contains_entity(json_object):
    QA_list = []

    for cluster in json_object['cluster']:
        if json_object['cluster'][cluster]['name']:
            ans_list = [json_object['entity'][x]['name'] for x in json_object['cluster'][cluster]['include_entity']]
            ans_list = sorted(ans_list)
            QA_ = {
                'question': 'Which entities are contained in cluster \'%s\'? ' % (json_object['cluster'][cluster]['name']) + '\n' + retrieval_format_instruction,
                'answer': ans_list,
                'metadata': {
                    'type': 'fill_in_the_blank',
                    'sub_type': 'certain_cluster_contains_entity',
                    'difficulty': 'intermediate',
                }
            }
            QA_list.append(QA_)

    return QA_list

# What is the label on the relation between Entity A and Entity B?
def generate_label_on_the_relation(json_object):
    QA_list = []

    for relation in json_object['relation']:
        ans = relation['name']
        if ans:
            source = relation['source']
            target = relation['target']
            QA_ = None
            if source in json_object['entity'] and target in json_object['entity']:
                source_name = json_object['entity'][relation['source']]['name']
                target_name = json_object['entity'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        'question': 'What is the label on the relation between Entity \'%s\' and Entity \'%s\'?' % (source_name, target_name) + '\n' + retrieval_format_instruction,
                        'answer': [ans],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation',
                            'difficulty': 'intermediate',
                            'challenge': 'label_detection'
                        }
                    }
            elif source in json_object['cluster'] and target in json_object['entity']:
                source_name = json_object['cluster'][relation['source']]['name']
                target_name = json_object['entity'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        'question': 'What is the label on the relation between Cluster \'%s\' and Entity \'%s\'?' % (source_name, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [ans],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation',
                            'difficulty': 'intermediate',
                            'challenge': 'label_detection'
                        }
                    }
            elif source in json_object['entity'] and target in json_object['cluster']:
                source_name = json_object['entity'][relation['source']]['name']
                target_name = json_object['cluster'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        'question': 'What is the label on the relation between Entity \'%s\' and Cluster \'%s\'?' % (source_name, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [ans],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation',
                            'difficulty': 'intermediate',
                            'challenge': 'label_detection'
                        }
                    }
            elif source in json_object['cluster'] and target in json_object['cluster']:
                source_name = json_object['cluster'][relation['source']]['name']
                target_name = json_object['cluster'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        'question': 'What is the label on the relation between Cluster \'%s\' and Cluster \'%s\'?' % (source_name, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [ans],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation',
                            'difficulty': 'intermediate',
                            'challenge': 'label_detection'
                        }
                    }
            if QA_:
                QA_list.append(QA_)
    return QA_list


# The label on the relation between Entity _____  and Entity ‘Search index’ is ‘Query’
# The label on the relation between Entity ‘Search index’  and Entity _____ is ‘Query’
def generate_labeled_relation_between_certain_elements(json_object):
    QA_list = []

    for relation in json_object['relation']:
        relation_label = relation['name']
        source = relation['source']
        target = relation['target']
        if relation_label:
            if source in json_object['entity'] and target in json_object['entity']:
                source_name = json_object['entity'][relation['source']]['name']
                target_name = json_object['entity'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        # 'question': 'The label on the relation between Entity ______ and Entity \'%s\' is \'%s\'' % (target_name, relation_label),
                        'question': 'Which entity has a relation with label \'%s\' to Entity \'%s\'?' % (relation_label, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [source_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_source',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)

                    QA_ = {
                        # 'question': 'The label on the relation between Entity \'%s\' and Entity ______ is \'%s\'' % (source_name, relation_label),
                        'question': 'Which entity has a relation with label \'%s\' from Entity \'%s\'? ' % (relation_label, source_name)  + '\n' + retrieval_format_instruction,
                        'answer': [target_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_target',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)

            elif source in json_object['cluster'] and target in json_object['entity']:
                source_name = json_object['cluster'][relation['source']]['name']
                target_name = json_object['entity'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        # 'question': 'The label on the relation between Cluster ______ and Entity \'%s\' is \'%s\'' % (target_name, relation_label),
                        'question': 'Which cluster has a relation with label \'%s\' to Entity \'%s\'?' % (relation_label, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [source_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_source',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)

                    QA_ = {
                        # 'question': 'The label on the relation between Cluster \'%s\' and Entity ______ is \'%s\'' % (source_name, relation_label),
                        'question': 'Which entity has a relation with label \'%s\' from Cluster \'%s\'?' % (relation_label, source_name)  + '\n' + retrieval_format_instruction,
                        'answer': [target_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_target',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)
            elif source in json_object['entity'] and target in json_object['cluster']:
                source_name = json_object['entity'][relation['source']]['name']
                target_name = json_object['cluster'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        # 'question': 'The label on the relation between Entity ______ and Cluster \'%s\' is \'%s\'' % (target_name, relation_label),
                        'question': 'Which entity has a relation with label \'%s\' to Cluster \'%s\'?' % (relation_label, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [source_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_source',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)

                    QA_ = {
                        # 'question': 'The label on the relation between Entity \'%s\' and Cluster ______ is \'%s\'' % (source_name, relation_label),
                        'question': 'Which cluster has a relation with label \'%s\' from Entity \'%s\'?' % (relation_label, source_name)  + '\n' + retrieval_format_instruction,
                        'answer': [target_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_target',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)
            elif source in json_object['cluster'] and target in json_object['cluster']:
                source_name = json_object['cluster'][relation['source']]['name']
                target_name = json_object['cluster'][relation['target']]['name']
                if source_name and target_name:
                    QA_ = {
                        # 'question': 'The label on the relation between Cluster ______ and Cluster \'%s\' is \'%s\'' % (target_name, relation_label),
                        'question': 'Which cluster has a relation with label \'%s\' to Cluster \'%s\'?' % (relation_label, target_name)  + '\n' + retrieval_format_instruction,
                        'answer': [source_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_source',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)

                    QA_ = {
                        # 'question': 'The label on the relation between Cluster \'%s\' and Cluster ______ is \'%s\'' % (source_name, relation_label),
                        'question': 'Which cluster has a relation with label \'%s\' to Cluster \'%s\'?' % (relation_label, source_name)  + '\n' + retrieval_format_instruction,
                        'answer': [target_name],
                        'metadata': {
                            'type': 'fill_in_the_blank',
                            'sub_type': 'label_on_the_relation_target',
                            'challenge': 'label_detection'
                        }
                    }
                    QA_list.append(QA_)
    return QA_list

# Cluster ____ contains Entity A.
def generate_cluster_contains_certain_entity(json_object):
    QA_list = []


    for entity in json_object['entity']:
        ans_list = []
        for cluster in json_object['cluster']:
            if entity in json_object['cluster'][cluster]['include_entity']:
                if json_object['cluster'][cluster]['name']:
                    ans_list.append(json_object['cluster'][cluster]['name'])

        ans_list = list(set(ans_list))
        ans_list = sorted(ans_list)
        if ans_list:
            QA_ = {
                'question': 'Which cluster(s) contain Entity \'%s\'?' %
                            (json_object['entity'][entity]['name'])  + '\n' + retrieval_format_instruction,
                'answer': ans_list,
                'metadata': {
                    'type': 'fill_in_the_blank',
                    'sub_type': 'cluster_contains_certain_entity',
                    'difficulty': 'intermediate',
                }
            }
            QA_list.append(QA_)

    return QA_list


# Entity A has an attribute named _____.
def generate_entity_contains_certain_attribute(json_object):
    QA_list = []

    for entity in json_object['entity']:
        entity_name = json_object['entity'][entity]['name']
        if 'attribute' in json_object['entity'][entity]:
            if json_object['diagram_type'] == 'structural':
                attribute_list = json_object['entity'][entity]['attribute']
            elif json_object['diagram_type'] == 'ER':
                attribute_list = [x[1] for x in json_object['entity'][entity]['attribute']]
            else:
                attribute_list = []
            ans_list = attribute_list
            ans_list = sorted(ans_list)
            if ans_list:
                QA_ = {
                    'question': 'What attributes does Entity \'%s\' have?' % (entity_name)  + '\n' + retrieval_format_instruction,
                    'answer': ans_list,
                    'metadata': {
                        'type': 'fill_in_the_blank',
                        'sub_type': 'entity_contains_certain_attribute',
                        'difficulty': 'intermediate',
                    }
                }
                QA_list.append(QA_)

    return QA_list


# Entity A has a method named _____.
def generate_entity_contains_certain_method(json_object):
    QA_list = []

    for entity in json_object['entity']:
        entity_name = json_object['entity'][entity]['name']
        if 'method' in json_object['entity'][entity]:
            attribute_list = json_object['entity'][entity]['method']
            ans_list = attribute_list
            ans_list = sorted(ans_list)
            if ans_list:
                QA_ = {
                    'question': 'What methods does Entity \'%s\' have? Please only the return function names.' % (entity_name)  + '\n' + retrieval_format_instruction,
                    'answer': ans_list,
                    'metadata': {
                        'type': 'fill_in_the_blank',
                        'sub_type': 'entity_contains_certain_method',
                        'difficulty': 'intermediate',
                    }
                }
                QA_list.append(QA_)

    return QA_list



# The type of the relation between Entity A and Entity B is _____
def generate_type_on_the_relation(json_object):
    QA_list = []
    if json_object['diagram_type'] == 'behavior':
        for relation in json_object['relation']:
            ans = relation['direction'] if 'direction' in relation else None
            if ans:
                source = relation['source']
                target = relation['target']
                QA_ = None
                if source in json_object['entity'] and target in json_object['entity']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the directionality of the relation between Entity \'%s\' and Entity \'%s\'? (e.g. single, double, and none)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['entity']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the directionality of the relation between Cluster \'%s\' and Entity \'%s\'? (e.g. single, double, and none)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['entity'] and target in json_object['cluster']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the directionality of the relation between Entity \'%s\' and Cluster \'%s\'? (e.g. single, double, and none)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['cluster']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the directionality of the relation between Cluster \'%s\' and Cluster \'%s\'? (e.g. single, double, and none)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                if QA_:
                    QA_list.append(QA_)
    elif json_object['diagram_type'] == 'structural':
        for relation in json_object['relation']:
            ans = relation['type'] if 'type' in relation else None
            if ans:
                source = relation['source']
                target = relation['target']
                QA_ = None
                if source in json_object['entity'] and target in json_object['entity']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the type of the relation between Entity \'%s\' and Entity \'%s\'? (e.g., association, inheritance, composition, dependency, and aggregation)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['entity']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the type of the relation between Cluster \'%s\' and Entity \'%s\'? (e.g., association, inheritance, composition, dependency, and aggregation)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['entity'] and target in json_object['cluster']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the type of the relation between Entity \'%s\' and Cluster \'%s\'? (e.g., association, inheritance, composition, dependency, and aggregation)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['cluster']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the type of the relation between Cluster \'%s\' and Cluster \'%s\'? (e.g., association, inheritance, composition, dependency, and aggregation)' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                if QA_:
                    QA_list.append(QA_)
    elif json_object['diagram_type'] == 'ER':
        for relation in json_object['relation']:
            if 'source_cardinality' in relation and 'target_cardinality' in relation:
                ans = [relation['source_cardinality'], relation['target_cardinality']]
            else:
                ans = None
            # ans = relation['type'] if 'type' in relation else None
            if ans:
                source = relation['source']
                target = relation['target']
                QA_ = None
                if source in json_object['entity'] and target in json_object['entity']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the cardinality on both sides of the relation between Entity \'%s\' and Entity \'%s\'? '
                                        '(For each side of the relation, please return \'zero or one\', \'exactly one\', \'one or more\', and \'zero or more\')' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['entity']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['entity'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the cardinality on both sides of the relation between Cluster \'%s\' and Entity \'%s\'?'
                                        '(For each side of the relation, please return \'zero or one\', \'exactly one\', \'one or more\', and \'zero or more\')' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['entity'] and target in json_object['cluster']:
                    source_name = json_object['entity'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the cardinality on both sides of the relation between Entity \'%s\' and Cluster \'%s\'?'
                                        '(For each side of the relation, please return \'zero or one\', \'exactly one\', \'one or more\', and \'zero or more\')' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                elif source in json_object['cluster'] and target in json_object['cluster']:
                    source_name = json_object['cluster'][relation['source']]['name']
                    target_name = json_object['cluster'][relation['target']]['name']
                    if source_name and target_name:
                        QA_ = {
                            'question': 'What is the cardinality on both sides of the relation between Cluster \'%s\' and Cluster \'%s\'?'
                                        '(For each side of the relation, please return \'zero or one\', \'exactly one\', \'one or more\', and \'zero or more\')' % (
                                source_name, target_name)  + '\n' + retrieval_format_instruction,
                            'answer': [ans],
                            'metadata': {
                                'type': 'fill_in_the_blank',
                                'sub_type': 'type_on_the_relation',
                                'difficulty': 'intermediate',
                                'challenge': 'label_detection'
                            }
                        }
                if QA_:
                    QA_list.append(QA_)

    return QA_list


# Entity _____ is the source in the relation with Entity A.
def generate_relation_source(json_object):
    QA_list = []
    entity_list = list(json_object['entity'])

    true_statement_dict = {}
    for relation in json_object['relation']:
        source = relation['source']
        target = relation['target']
        if source in json_object['entity'] and target in json_object['entity']:
            if target not in true_statement_dict:
                true_statement_dict[target] = [source]
            else:
                true_statement_dict[target].append(source)

    for entity1 in true_statement_dict:
        ans_list = [json_object['entity'][x]['name'] for x in true_statement_dict[entity1]]
        ans_list = sorted(ans_list)
        QA_ = {
            'question': 'Which entity is the source in a relation to Entity \'%s\'?' % (
            json_object['entity'][entity1]['name'])  + '\n' + retrieval_format_instruction,
            'answer': ans_list,
            'metadata': {
                'type': 'fill_in_the_blank',
                'sub_type': 'relation_source',
                'difficulty': 'intermediate',
                'challenge': 'label_detection'
            }
        }
        QA_list.append(QA_)

    return QA_list

# Entity _____ is the target in the relation with Entity A.
def generate_relation_target(json_object):
    QA_list = []
    entity_list = list(json_object['entity'])

    true_statement_dict = {}
    for relation in json_object['relation']:
        source = relation['source']
        target = relation['target']
        if source in json_object['entity'] and target in json_object['entity']:
            if source not in true_statement_dict:
                true_statement_dict[source] = [target]
            else:
                true_statement_dict[source].append(target)
    # print(true_statement_dict)
    for entity1 in true_statement_dict:
        ans_list = [json_object['entity'][x]['name'] for x in true_statement_dict[entity1]]
        ans_list = sorted(ans_list)
        QA_ = {
            'question': 'Which entity is the target in a relation from Entity \'%s\'?' % (
                json_object['entity'][entity1]['name'])  + '\n' + retrieval_format_instruction,
            'answer': ans_list,
            'metadata': {
                'type': 'fill_in_the_blank',
                'sub_type': 'relation_target',
                'difficulty': 'intermediate',
                'challenge': 'label_detection'
            }
        }
        QA_list.append(QA_)

    return QA_list


# ---------------------multiple elements in the answer-------------------------------

# # Entity A has relations with Entities _____.
# def generate_certain_entity_has_relations_with(json_object):
#     QA_list = []
#
#     ans_pair_list = find_certain_entity_has_a_relation_with_others(json_object)
#     for ans_pair in ans_pair_list:
#         entity_name, ans_list, wrong_options_list = ans_pair
#         ans_list = sorted(list(set(ans_list)))
#         QA_ = {
#             'question': 'Entity \'%s\' has relations with Entities _____. (Please specify all the entities)' % (json_object['entity'][entity_name]['name']),
#             'answer': [ans_list],
#             'metadata': {
#                 'type': 'fill_in_the_blank',
#                 'sub_type': 'certain_entity_has_relations_with',
#                 'difficulty': 'basic',
#                 'multiple_elements': True,
#             }
#         }
#         QA_list.append(QA_)
#
#     return QA_list

# # Cluster A contains Entities _____.
# def generate_certain_cluster_contains_entities(json_object):
#     QA_list = []
#
#     for cluster in json_object['cluster']:
#         if json_object['cluster'][cluster]['name']:
#             ans_list = [json_object['entity'][x]['name'] for x in json_object['cluster'][cluster]['include_entity']]
#             ans_list = sorted(list(set(ans_list)))
#             QA_ = {
#                 'question': 'Cluster \'%s\' contains Entities ______. (Please specify all the entities)' %
#                             (json_object['cluster'][cluster]['name']),
#                 'answer': [ans_list],
#                 'metadata': {
#                     'type': 'fill_in_the_blank',
#                     'sub_type': 'certain_cluster_contains_entities',
#                     'difficulty': 'intermediate',
#                     'multiple_elements': True,
#                 }
#             }
#             QA_list.append(QA_)
#
#     return QA_list

# Which relation has the label 'search'? ______
def generate_which_relation_has_certain_label(json_object):
    QA_list = []

    for relation in json_object['relation']:
        if 'name' in relation and relation['name']:
            label = relation['name']
            source = relation['source']
            target = relation['target']
            if source in json_object['entity'] and target in json_object['entity']:
                source_name = json_object['entity'][source]['name']
                target_name = json_object['entity'][target]['name']
                ans = (source_name, target_name)
                QA_ = {
                    'question': 'Which relation(s) carry the label \'%s\'? '
                                'Please use format [source entity, target entity] to represent certain relation.' % (label)  + '\n' +
                                retrieval_format_instruction,
                    'answer': [ans],
                    'metadata': {
                        'type': 'fill_in_the_blank',
                        'sub_type': 'which_relation_has_certain_label',
                        'difficulty': 'intermediate',
                    }
                }
                QA_list.append(QA_)

    return QA_list


def length_control(x_list, target_len=1):
    if target_len == -1:
        return x_list
    if len(x_list) == 0:
        return x_list
    if len(x_list) > target_len:
        return x_list[:target_len]
    return x_list


# with open('./dataset/SAD_backup/behavior/ai-search-skillsets.json', 'r') as f:
#     json_object = json.load(f)


# QA_list0 = generate_fill_in_the_blank_relation_source(json_object)

def main():
    options = [
        'generate_total_entity_number',
        'generate_total_relation_number',
        'generate_entities_have_more_than_one_relations',
        'generate_total_cluster_number',
        'generate_how_many_entities_not_in_clusters',
        'generate_how_many_relations_have_label',
        'generate_how_many_clusters_have_clusters_within',
        'generate_how_many_entities_does_certain_cluster_have',
        'generate_how_many_relation_types',
        'generate_how_many_attributes_certain_entity_has',
        'generate_how_many_methods_certain_entity_has',

        'generate_cluster_has_most_entities',
        'generate_relation_statement',
        # 'generate_two_entities_in_the_same_cluster', # removed because of ambiguity
        'generate_certain_cluster_contains_entity',
        'generate_label_on_the_relation',
        'generate_labeled_relation_between_certain_elements',
        'generate_cluster_contains_certain_entity',
        'generate_entity_contains_certain_attribute',
        'generate_entity_contains_certain_method',
        'generate_type_on_the_relation',
        'generate_relation_source',
        'generate_relation_target',
        'generate_which_relation_has_certain_label'
    ]
    prompt_option = 'zero-shot' # 'one-shot', 'few-shot'

    # QA_list = []
    sum = 0
    diagram_type_list = ['behavior', 'structural', 'ER']
    # diagram_type_list = ['ER']
    for diagram_type in diagram_type_list:
        path = f'../../dataset/SAD/{diagram_type}/json_object/'
        file_list = os.listdir(path)

        for file in file_list:
            QA_list = []
            source_path = path + file
            target_path = path.replace('json_object', 'QA') + file.replace('.json', '_QA.json')
            with open(source_path, 'r') as f:
                json_object = json.load(f)

            if 'generate_total_entity_number' in options:
                tmp_list = generate_total_entity_number(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_total_relation_number' in options:
                tmp_list = generate_total_relation_number(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_entities_have_more_than_one_relations' in options:
                tmp_list = generate_entities_have_more_than_one_relations(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_total_cluster_number' in options:
                tmp_list = generate_total_cluster_number(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_cluster_has_most_entities' in options:
                tmp_list = generate_cluster_has_most_entities(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_entities_not_in_clusters' in options:
                tmp_list = generate_how_many_entities_not_in_clusters(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_relations_have_label' in options:
                tmp_list = generate_how_many_relations_have_label(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_clusters_have_clusters_within' in options:
                tmp_list = generate_how_many_clusters_have_clusters_within(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_entities_does_certain_cluster_have' in options:
                tmp_list = generate_how_many_entities_does_certain_cluster_have(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_relation_types' in options:
                tmp_list = generate_how_many_relation_types(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_relation_statement' in options:
                tmp_list = generate_relation_statement(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_two_entities_in_the_same_cluster' in options:
                tmp_list = generate_two_entities_in_the_same_cluster(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_certain_cluster_contains_entity' in options:
                tmp_list = generate_certain_cluster_contains_entity(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_label_on_the_relation' in options:
                tmp_list = generate_label_on_the_relation(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_labeled_relation_between_certain_elements' in options:
                tmp_list = generate_labeled_relation_between_certain_elements(json_object)
                QA_list += length_control(tmp_list, 2)
            if 'generate_cluster_contains_certain_entity' in options:
                tmp_list = generate_cluster_contains_certain_entity(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_entity_contains_certain_attribute' in options:
                tmp_list = generate_entity_contains_certain_attribute(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_entity_contains_certain_method' in options:
                tmp_list = generate_entity_contains_certain_method(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_attributes_certain_entity_has' in options:
                tmp_list = generate_how_many_attributes_certain_entity_has(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_how_many_methods_certain_entity_has' in options:
                tmp_list = generate_how_many_methods_certain_entity_has(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_type_on_the_relation' in options:
                tmp_list = generate_type_on_the_relation(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_relation_source' in options:
                tmp_list = generate_relation_source(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_relation_target' in options:
                tmp_list = generate_relation_target(json_object)
                QA_list += length_control(tmp_list)
            if 'generate_which_relation_has_certain_label' in options:
                tmp_list = generate_which_relation_has_certain_label(json_object)
                QA_list += length_control(tmp_list)

            with open(target_path, "w") as f:
                json.dump(QA_list, f, indent=4)
            sum += len(QA_list)