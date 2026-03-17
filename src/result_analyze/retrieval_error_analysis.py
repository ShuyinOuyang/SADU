from util import *
from collections import Counter

def compare_response_and_answer(response, answer):
    # print(response, answer)
    try:
        ca = Counter(response)
        cb = Counter(answer)

        # multiset subset checks (duplicates matter)
        a_is_subset_b = all(ca[k] <= cb[k] for k in ca)
        b_is_subset_a = all(cb[k] <= ca[k] for k in cb)

        if a_is_subset_b:
            return 'response_is_subset_answer', list((ca & cb).elements()), sum((ca & cb).values())

        elif b_is_subset_a:
            return 'response_is_superset_answer', list((ca & cb).elements()), sum((ca & cb).values())

        else:
            overlap_counter = ca & cb  # keeps min frequency for each element
            overlap_list = list(overlap_counter.elements())
            overlap_count = sum(overlap_counter.values())
            return "Neither is a subset", overlap_list, overlap_count
    except:
        # print('ERROR')
        pass

def process(statistic_dic, diagram_type):
    exact_match = 0
    subset_num = 0
    superset_num = 0
    otherset_num = 0
    missing_count_list = []
    spurious_count_list = []

    precision_list = []
    recall_list = []
    F1_list = []

    total = 0

    # result_dic = {
    #     'behavior': {
    #         'exact_match': 0,
    #         'subset_num': 0,
    #         'superset_num': 0,
    #         'otherset_num': 0,
    #         'missing_count': 0,
    #         'spurious_count': 0,
    #         'total': 0,
    #         'precision_list': [],
    #         'recall_list': [],
    #         'F1_list': []
    #     },
    #     'structural': {
    #         'exact_match': 0,
    #         'subset_num': 0,
    #         'superset_num': 0,
    #         'otherset_num': 0,
    #         'missing_count': 0,
    #         'spurious_count': 0,
    #         'total': 0,
    #         'precision_list': [],
    #         'recall_list': [],
    #         'F1_list': []
    #     },
    #     'ER':{
    #         'exact_match': 0,
    #         'subset_num': 0,
    #         'superset_num': 0,
    #         'otherset_num': 0,
    #         'missing_count': 0,
    #         'spurious_count': 0,
    #         'total': 0,
    #         'precision_list': [],
    #         'recall_list': [],
    #         'F1_list': []
    #     },
    #     'all': {
    #         'exact_match': 0,
    #         'subset_num': 0,
    #         'superset_num': 0,
    #         'otherset_num': 0,
    #         'missing_count': 0,
    #         'spurious_count': 0,
    #         'total': 0,
    #         'precision_list': [],
    #         'recall_list': [],
    #         'F1_list': []
    #     }
    # }


    for QA_type in statistic_dic[diagram_type]:
        for x in statistic_dic[diagram_type][QA_type]:
            if check_counting_or_retrieval(QA_type) == 'retrieval':
                total += 1
                response_final = response_processing(x['response'])
                try:
                    response = json.loads(response_final)['answer']
                except:
                    continue
                answer = x['answer']
                if x['metadata']['sub_type'] in ['type_on_the_relation'] and x['diagram_type'] == 'ER':
                    # if response == answer[0]:
                    answer = answer[0]
                elif x['metadata']['sub_type'] in ['entity_contains_certain_method']:
                    response = [x.replace('()', '') for x in response]
                    response = sorted(response)
                    answer = sorted(answer)
                elif x['metadata']['sub_type'] in ['which_relation_has_certain_label']:
                    try:
                        if isinstance(response, list) and len(response) > 0:
                            response = response[0]
                        if isinstance(response, str) and '[' in response and ']' in response:
                            response = eval(response)
                    except:
                        response = json.loads(response_final)['answer']
                        # response = [x[0].replace('()', '') for x in response]
                    answer = answer[0]
                else:
                    response = sorted(response)
                    answer = sorted(answer)

                if response == answer:
                    # exact match rate
                    exact_match += 1
                    overlap_list, overlap_count = response, len(response)
                else:
                    try:
                        res, overlap_list, overlap_count = compare_response_and_answer(response, answer)
                        # print(res, overlap_list, overlap_count)
                    except:
                        continue
                    # subset rate & superset rate
                    if res == 'response_is_subset_answer':
                        subset_num += 1
                    elif res == 'response_is_superset_answer':
                        superset_num += 1
                    else:
                        otherset_num += 1
                if len(response):
                    precision = overlap_count / len(response)
                else:
                    precision = 0
                recall = overlap_count / len(answer)
                if precision and recall:
                    F1 = 2 * precision * recall / (precision + recall)
                else:
                    F1 = 0
                precision_list.append(precision)
                recall_list.append(recall)
                F1_list.append(F1)
                missing_count_list.append(len(answer) - overlap_count)
                spurious_count_list.append(len(response) - overlap_count)

    missing_count_list = [x for x in missing_count_list if x != 0]
    spurious_count_list = [x for x in spurious_count_list if x != 0]
    res = {
        'precision': np.mean(precision_list),
        'recall': np.mean(recall_list),
        'F1': np.mean(F1_list),
        'exact_match_rate': exact_match/total,
        'subset_rate': subset_num/total,
        'superset_rate': superset_num/total,
        'otherset_rate': otherset_num/total,
        'missing_count': np.mean(missing_count_list),
        'spurious_count': np.mean(spurious_count_list),
        'total': total
    }

    return res
    # print(np.mean(precision_list), np.mean(recall_list), np.mean(F1_list))



def retrieval_problem_error_analysis_by_model():
    log_file_dic = {
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

    diagram_type_list = ["behavior", "structural", "ER", "all"]
    diagram_type = diagram_type_list[3]

    # print('%s & %s & %s & %s \\\\' % ('Diagram Type', 'Exact Match', 'Acc@1', 'Acc@2'))
    for file in log_file_dic:

        statistic_dic = generate_statistic_dic_all(file)
        result_dic = {
            'behavior': process(statistic_dic, diagram_type),
            'structural': process(statistic_dic, diagram_type),
            'ER': process(statistic_dic, diagram_type),
            'all': process(statistic_dic, diagram_type)
        }
        print('%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\' %
              (log_file_dic[file],
               result_dic['all']['precision'],
               result_dic['all']['recall'],
               result_dic['all']['F1'],
               result_dic['all']['exact_match_rate'],
               result_dic['all']['subset_rate'],
               result_dic['all']['superset_rate'],
               result_dic['all']['missing_count'],
               result_dic['all']['spurious_count'],
               ))

        # result_dic = {}
        # for diagram_type in diagram_type_list:
        #     result_dic[diagram_type] = {}
        #
        # for diagram_type in diagram_type_list:
        #     exact_match, pass_with_tolerance1, pass_with_tolerance2, total = exactness_tolerance(statistic_dic, diagram_type)
        #     result_dic[diagram_type] = {
        #         'Exact Match': exact_match / total,
        #         'Acc@$\pm$1': (exact_match + pass_with_tolerance1) / total,
        #         'Acc@$\pm$2': (exact_match + pass_with_tolerance2) / total,
        #     }
        #     # print('%s & %.2f & %.2f & %.2f \\\\' % (diagram_type, exact_match/total, (exact_match + pass_with_tolerance1)/total, (exact_match + pass_with_tolerance2)/total))
        #
        # print('%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\' %
        #       (log_file_dic[file],
        #        result_dic['behavior']['Exact Match'], result_dic['behavior']['Acc@$\pm$1'],
        #        result_dic['behavior']['Acc@$\pm$2'],
        #        result_dic['structural']['Exact Match'], result_dic['structural']['Acc@$\pm$1'],
        #        result_dic['structural']['Acc@$\pm$2'],
        #        result_dic['ER']['Exact Match'], result_dic['ER']['Acc@$\pm$1'], result_dic['ER']['Acc@$\pm$2'],
        #        result_dic['all']['Exact Match'], result_dic['all']['Acc@$\pm$1'], result_dic['all']['Acc@$\pm$2']))

retrieval_problem_error_analysis_by_model()

def retrieval_problem_error_analysis_by_answer_size():
    file = '512/gemini-2.5-flash_response_0223_t_0.log'
    diagram_type_list = ["behavior", "structural", "ER", "all"]
    diagram_type = diagram_type_list[3]

    statistic_dic = generate_statistic_dic_all(file)
    result_dic = {
        'behavior': process(statistic_dic, diagram_type),
        'structural': process(statistic_dic, diagram_type),
        'ER': process(statistic_dic, diagram_type),
        'all': process(statistic_dic, diagram_type)
    }


# TODO:
#   1. set-based metrics
#       (a) precision, recall, F1
#       (b) exact set match, subset rate, superset rate
#       (c) missing counting, spurious counting -> to answer “does the model mostly miss correct entities, or does it hallucinate extras?"
#   2. slide the performance by difficulty factors
#       (a) gold set size |G_i| (Many retrieval questions have 1 answer, some have many. Performance often collapses as |G_i| grows)
#       (b) Diagram complexity, |V|, |E|
#   3. Qualitative taxonomy
#       (a) Under-retrieval, Over-retrieval
#       (b) directionality confusion
#       (c) Relation-type confusion

