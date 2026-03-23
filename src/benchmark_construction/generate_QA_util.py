import random
random.seed(42)


def calculate_how_many_entities_have_more_than_one_relations(json_object):
    record_dict = {}
    for r in json_object['relation']:
        if r['source'] not in record_dict:
            record_dict[r['source']] = 0
        else:
            record_dict[r['source']] += 1

        if r['target'] not in record_dict:
            record_dict[r['target']] = 0
        else:
            record_dict[r['target']] += 1

    final_count = 0
    for key in record_dict:
        if record_dict[key] >= 1:
            final_count += 1
    return final_count

def find_which_cluster_has_the_most_relations(json_object):
    record_dict = []
    candidates_list = []
    ans = ''
    for cluster in json_object['cluster']:
        include_entity_num = len(json_object['cluster'][cluster]['include_entity'])
        record_dict.append([cluster, include_entity_num])

    # get the cluster with max num and name
    record_dict = sorted(record_dict, key=lambda x: x[1], reverse=True)
    ans_flag = True
    max_cluster_num = 0
    for x in record_dict:
        if x[1] == max_cluster_num:
            continue
        if ans_flag and json_object['cluster'][x[0]]['name']:
            ans = json_object['cluster'][x[0]]['name']
            max_cluster_num = x[1]
            ans_flag = False
        candidates_list.append(json_object['cluster'][x[0]]['name'])

    return ans, candidates_list

def find_which_cluster_has_the_most_clusters(json_object):
    record_dict = []
    candidates_list = []
    ans_list = []
    for cluster in json_object['cluster']:
        include_entity_num = len(json_object['cluster'][cluster]['include_entity'])
        record_dict.append([cluster, include_entity_num])

    # get the cluster with max num and name
    record_dict = sorted(record_dict, key=lambda x: x[1], reverse=True)
    # print(record_dict)
    if record_dict:
        max_cluster_num =  record_dict[0][1]

        for x in record_dict:
            if x[1] == max_cluster_num:
                if json_object['cluster'][x[0]]['name']:
                    ans_list.append(json_object['cluster'][x[0]]['name'])
            candidates_list.append(json_object['cluster'][x[0]]['name'])

        return ans_list, candidates_list
    else:
        return [], []

def calculate_how_many_entities_not_in_clusters(json_object):
    ans = 0

    in_cluster_entities = []
    for cluster in json_object['cluster']:
        in_cluster_entities += json_object['cluster'][cluster]['include_entity']

    in_cluster_entities = list(set(in_cluster_entities))

    for entity in json_object['entity']:
        if entity not in in_cluster_entities:
            ans += 1
    return ans


def calculate_how_many_relations_have_label(json_object):
    ans = 0

    for r in json_object['relation']:
        if r['name']:
            ans += 1

    return ans

def calculate_how_many_clusters_have_clusters_within(json_object):
    ans = 0

    for cluster in json_object['cluster']:
        if json_object['cluster'][cluster]['include_cluster']:
            ans += 1

    return ans


def find_how_many_entities_does_certain_cluster_have(json_object):
    entity_ans_pair_list = []
    for cluster in json_object['cluster']:
        # cluster, cluster_name, entity_count
        entity_ans_pair_list.append((cluster,
                                     json_object['cluster'][cluster]['name'],
                                     len(json_object['cluster'][cluster]['include_entity']))
                                    )

    return entity_ans_pair_list


def calculate_how_many_relation_types(json_object):
    # ans = 0
    relation_types = set()
    for relation in json_object['relation']:
        if 'type' in relation:
            relation_types.add(relation['type'])
        elif 'direction' in relation:
            relation_types.add(relation['direction'])

    ans = len(relation_types)
    return ans

def find_certain_entity_has_a_relation_with_others(json_object):
    ans_pair_list = []
    relation_dict = {}
    entity_list = []
    for relation in json_object['relation']:
        if relation['source'] not in relation_dict:
            if relation['source'] in json_object['entity'] and relation['target'] in json_object['entity']:
                relation_dict[relation['source']] = [relation['target']]
        else:
            if relation['source'] in json_object['entity'] and relation['target'] in json_object['entity']:
                relation_dict[relation['source']].append(relation['target'])
        if relation['target'] not in relation_dict:
            if relation['source'] in json_object['entity'] and relation['target'] in json_object['entity']:
                relation_dict[relation['target']] = [relation['source']]
        else:
            if relation['source'] in json_object['entity'] and relation['target'] in json_object['entity']:
                relation_dict[relation['target']].append(relation['source'])

    for entity in json_object['entity']:
        entity_list.append(entity)

    for key in relation_dict:
        ans_list = [json_object['entity'][x]['name'] for x in relation_dict[key]]
        wrong_options_list = [json_object['entity'][x]['name'] for x in entity_list if x not in ans_list]
        ans_list = list(set(ans_list))
        # wrong_options_list = list(set(wrong_options_list))
        wrong_options_list = list(set([x for x in wrong_options_list if x not in ans_list]))
        # entity, ans, wrong options
        ans_pair_list.append((
            key, ans_list, wrong_options_list
        ))
    return ans_pair_list


def generate_false_statement_elation_statement(json_object, true_statement_dict):
    QA_list = []
    candidate_dict = {}
    # entity candidates
    for e in json_object['entity']:
        if e not in candidate_dict:
            candidate_dict[e] = json_object['entity'][e]

    for c in json_object['cluster']:
        if c not in candidate_dict:
            candidate_dict[c] = json_object['cluster'][c]


    for source in candidate_dict:
        for target in candidate_dict:
            if source == target:
                continue


            if 'entity' in source:
                source_name = json_object['entity'][source]['name']
                source_name_in_dict = 'Entity: %s' % json_object['entity'][source]['name']
            else:
                source_name = json_object['cluster'][source]['name']
                source_name_in_dict = 'Cluster: %s' % json_object['cluster'][source]['name']

            if 'entity' in target:
                target_name = json_object['entity'][target]['name']
                target_name_in_dict = 'Entity: %s' % json_object['entity'][target]['name']
            else:
                target_name = json_object['cluster'][target]['name']
                target_name_in_dict = 'Cluster: %s' % json_object['cluster'][target]['name']

            if (source_name_in_dict not in true_statement_dict) or (target_name_in_dict not in true_statement_dict[source_name_in_dict]):

                if 'Entity' in source_name_in_dict and 'Entity' in target_name_in_dict:

                    QA_ = {
                            'question': 'Entity \'%s\' has a relation with Entity \'%s\'.' % (source_name, target_name),
                            'answer': 'False',
                            'metadata': {
                                'type': 'true_or_false',
                                'sub_type': 'relation_statement',
                                'difficulty': 'basic',
                            }
                        }

                elif 'Entity' in source_name_in_dict and 'Cluster' in target_name_in_dict:
                    QA_ = {
                        'question': 'Entity \'%s\' has a relation with Cluster \'%s\'.' % (source_name, target_name),
                        'answer': 'False',
                        'metadata': {
                            'type': 'true_or_false',
                            'sub_type': 'relation_statement',
                            'difficulty': 'basic',
                        }
                    }

                elif 'Cluster' in source_name_in_dict and 'Entity' in target_name_in_dict:
                    QA_ = {
                        'question': 'Cluster \'%s\' has a relation with Entity \'%s\'.' % (source_name, target_name),
                        'answer': 'False',
                        'metadata': {
                            'type': 'true_or_false',
                            'sub_type': 'relation_statement',
                            'difficulty': 'basic',
                        }
                    }

                elif 'Cluster' in source_name_in_dict and 'Cluster' in target_name_in_dict:
                    QA_ = {
                        'question': 'Cluster \'%s\' has a relation with Cluster \'%s\'.' % (source_name, target_name),
                        'answer': 'False',
                        'metadata': {
                            'type': 'true_or_false',
                            'sub_type': 'relation_statement',
                            'difficulty': 'basic',
                        }
                    }
                else:
                    QA_ = {}
                if QA_:
                    QA_list.append(QA_)

    return QA_list


def generate_false_statement_two_entities_in_the_same_cluster(json_object, true_statement_dict):
    QA_list = []
    for entity1 in true_statement_dict:
        for entity2 in true_statement_dict:
            if entity1 == entity2:
                continue

            if entity2 not in entity1:
                QA_ = {
                    'question': 'Entity \'%s\' and Entity \'%s\' are in the same cluster.\n'
                                % (json_object['entity'][entity1]['name'],
                                   json_object['entity'][entity2]['name']),
                    'answer': 'False',
                    'metadata': {
                        'type': 'true_or_false',
                        'sub_type': 'two_entities_in_the_same_cluster',
                        'difficulty': 'intermediate',
                        'challenge': 'cluster'
                    }
                }
                QA_list.append(QA_)

    return QA_list


def generate_false_statement_two_entities_in_the_same_cluster_and_have_a_relation(json_object, true_statement_dict):
    QA_list = []
    for entity1 in true_statement_dict:
        for entity2 in true_statement_dict:
            if entity1 == entity2:
                continue
            if entity2 not in true_statement_dict[entity1] or true_statement_dict[entity1][entity2] != 1:
                QA_ = {
                    'question': 'Entity \'%s\' and Entity \'%s\' are in the same cluster and have a relation.\n' %
                                (json_object['entity'][entity1]['name'], json_object['entity'][entity2]['name']),
                    'answer': 'False',
                    'metadata': {
                        'type': 'true_or_false',
                        'sub_type': 'two_entities_in_the_same_cluster_and_have_a_relation',
                        'difficulty': 'intermediate',
                        'challenge': 'cluster'
                    }
                }
                QA_list.append(QA_)

    return QA_list


def generate_false_statement_two_entities_not_in_the_same_cluster_but_have_a_relation(json_object, true_statement_dict):
    QA_list = []
    for entity1 in true_statement_dict:
        for entity2 in true_statement_dict[entity1]:
            if true_statement_dict[entity1][entity2] != 2:
                QA_ = {
                    'question': 'Entity \'%s\' and Entity \'%s\' are not in the same cluster but have a relation.\n' %
                                (json_object['entity'][entity1]['name'], json_object['entity'][entity2]['name']),
                    'answer': 'False',
                    'metadata': {
                        'type': 'true_or_false',
                        'sub_type': 'two_entities_not_in_the_same_cluster_but_have_a_relation',
                        'difficulty': 'intermediate',
                        'challenge': 'cluster'
                    }
                }
                QA_list.append(QA_)

    return QA_list

def find_certain_cluster_contains_entity(json_object):
    ans_pair_list = []
    entity_list = list(json_object['entity'].keys())
    for cluster in json_object['cluster']:
        if 'name' not in json_object['cluster'][cluster]:
            continue
        ans_list = json_object['cluster'][cluster]['include_entity']
        ans_name_list = [json_object['entity'][x]['name'] for x in ans_list]
        wrong_options = [json_object['entity'][x]['name'] for x in entity_list if x not in ans_list]
        wrong_options = list(set([x for x in wrong_options if x not in ans_name_list]))
        for ans in ans_list:
            # cluster, ans, wrong options
            ans_pair_list.append((json_object['cluster'][cluster]['name'], json_object['entity'][ans]['name'], wrong_options))

    return ans_pair_list

def find_certain_cluster_contains_cluster(json_object):
    ans_pair_list = []
    for cluster in json_object['cluster']:
        if 'name' not in json_object['cluster'][cluster]:
            continue
        ans_list = json_object['cluster'][cluster]['include_cluster']
        if not ans_list:
            continue

        ans_name_list = [json_object['cluster'][x]['name'] for x in ans_list]
        wrong_options = [json_object['cluster'][x]['name'] for x in json_object['cluster'] if (x not in ans_list and json_object['cluster'][x]['name'])]
        wrong_options = list(set([x for x in wrong_options if x not in ans_name_list]))
        if len(wrong_options) < 3:
            continue
        for ans in ans_list:
            # cluster, ans, wrong options
            ans_pair_list.append((json_object['cluster'][cluster]['name'], json_object['cluster'][ans]['name'], wrong_options))

    return ans_pair_list

def generate_false_statement_relation_between_entities_of_different_cluster(json_object, true_statement_dict):
    QA_list = []
    for cluster1 in json_object['cluster']:
        for cluster2 in json_object['cluster']:
            if cluster1 == cluster2:
                continue
            if (cluster1 in true_statement_dict and
                    cluster2 in true_statement_dict[cluster1] and
                    true_statement_dict[cluster1][cluster2] == 1):
                continue
            cluster1_name = json_object['cluster'][cluster1]['name']
            cluster2_name = json_object['cluster'][cluster2]['name']
            QA_ = {
                'question': 'There is at least one relation between entities of Cluster \'%s\' and entities of Cluster \'%s\'.' %
                            (cluster1_name, cluster2_name),
                'answer': 'False',
                'metadata': {
                    'type': 'true_or_false',
                    'sub_type': 'relation_between_entities_of_different_cluster',
                    'difficulty': 'intermediate',
                    'challenge': 'cluster'
                }
            }
            QA_list.append(QA_)

    return QA_list


def find_two_entities_in_the_same_cluster(json_object):
    entity_in_the_same_cluster_dict = {}
    for entity1 in json_object['entity']:
        entity_in_the_same_cluster_dict[entity1] = {}
        for entity2 in json_object['entity']:
            if entity1 != entity2:
                entity_in_the_same_cluster_dict[entity1][entity2] = 0

    for cluster in json_object['cluster']:
        include_entity_list = json_object['cluster'][cluster]['include_entity']
        for entity1 in include_entity_list:
            for entity2 in include_entity_list:
                if entity1 != entity2:
                    entity_in_the_same_cluster_dict[entity1][entity2] = 1

    QA_pair = []
    for entity1 in json_object['entity']:
        ans_list = []
        for entity2 in entity_in_the_same_cluster_dict[entity1]:
            if entity_in_the_same_cluster_dict[entity1][entity2] != 1:
                ans_list.append(json_object['entity'][entity2]['name'])

        ans_list = list(set(ans_list))
        QA_pair.append((json_object['entity'][entity1]['name'], ans_list))


    return QA_pair

