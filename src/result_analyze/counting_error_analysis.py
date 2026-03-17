from util import *
base_path = '../../'



def statistic_table(file, diagram_type):
    statistic_dict = generate_statistic_dic(file)

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


            print('%s\t%s\t%s\t%.2f%%\t%s\t%.2f%%\t%s\t%.2f%%' %
                  (QA_sub_type,
                   len(statistic_dict[diagram_type][QA_sub_type]),
                   statistic_dict[diagram_type][QA_sub_type].count('True'),
                   true_rate * 100,
                   statistic_dict[diagram_type][QA_sub_type].count('False'),
                   false_rate * 100,
                   statistic_dict[diagram_type][QA_sub_type].count('Parse Error'),
                   parse_error_rate * 100
                   ))

    sum_total = sum([len(statistic_dict[diagram_type][QA_sub_type]) for QA_sub_type in statistic_dict[diagram_type]])
    sum_true = sum([statistic_dict[diagram_type][QA_sub_type].count('True') for QA_sub_type in statistic_dict[diagram_type]])
    sum_false = sum([statistic_dict[diagram_type][QA_sub_type].count('False') for QA_sub_type in statistic_dict[diagram_type]])
    sum_error = sum([statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type]])
    print('%s\t%s\t%s\t%.2f%%\t%s\t%.2f%%\t%s\t%.2f%%' %
          ("Total",
           sum_total,
           sum_true,
           sum_true/sum_total * 100,
           sum_false,
           sum_false/sum_total  * 100,
           sum_error,
           sum_error/sum_total  * 100
           ))


def exactness_tolerance(statistic_dic, diagram_type):
    exact_match = 0
    pass_with_tolerance1 = 0 # not including exact match
    pass_with_tolerance2 = 0  # not including exact match
    total = 0

    for QA_type in statistic_dic[diagram_type]:
        for x in statistic_dic[diagram_type][QA_type]:
            if check_counting_or_retrieval(QA_type) == 'counting':
                total += 1
                response_final = response_processing(x['response'])
                try:
                    response = json.loads(response_final)['answer']
                except:
                    continue
                answer = x['answer']
                if response == answer[0]:
                    exact_match += 1
                else:
                    if abs(response - answer[0]) <= 1:
                        pass_with_tolerance1 += 1
                    if abs(response - answer[0]) <= 2:
                        pass_with_tolerance2 += 1

    return exact_match, pass_with_tolerance1, pass_with_tolerance2, total


def counting_problem_error_analysis1():
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
    # diagram_type = diagram_type_list[0]

    # print('%s & %s & %s & %s \\\\' % ('Diagram Type', 'Exact Match', 'Acc@1', 'Acc@2'))
    for file in log_file_dic:
        statistic_dic = generate_statistic_dic_all(file)
        result_dic = {}
        for diagram_type in diagram_type_list:
            result_dic[diagram_type] = {}

        for diagram_type in diagram_type_list:
            exact_match, pass_with_tolerance1, pass_with_tolerance2, total = exactness_tolerance(statistic_dic,
                                                                                                 diagram_type)
            result_dic[diagram_type] = {
                'Exact Match': exact_match / total,
                'Acc@$\pm$1': (exact_match + pass_with_tolerance1) / total,
                'Acc@$\pm$2': (exact_match + pass_with_tolerance2) / total,
            }
            # print('%s & %.2f & %.2f & %.2f \\\\' % (diagram_type, exact_match/total, (exact_match + pass_with_tolerance1)/total, (exact_match + pass_with_tolerance2)/total))

        print('%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\' %
              (log_file_dic[file],
               result_dic['behavior']['Exact Match'], result_dic['behavior']['Acc@$\pm$1'],
               result_dic['behavior']['Acc@$\pm$2'],
               result_dic['structural']['Exact Match'], result_dic['structural']['Acc@$\pm$1'],
               result_dic['structural']['Acc@$\pm$2'],
               result_dic['ER']['Exact Match'], result_dic['ER']['Acc@$\pm$1'], result_dic['ER']['Acc@$\pm$2'],
               result_dic['all']['Exact Match'], result_dic['all']['Acc@$\pm$1'], result_dic['all']['Acc@$\pm$2']))


def MAE(statistic_dic, diagram_type):
    abs_diff = []

    for QA_type in statistic_dic[diagram_type]:
        for x in statistic_dic[diagram_type][QA_type]:
            if check_counting_or_retrieval(QA_type) == 'counting':
                # total += 1
                response_final = response_processing(x['response'])
                try:
                    response = json.loads(response_final)['answer']
                except:
                    continue
                answer = x['answer']
                abs_diff.append(abs(response - answer[0]))

    return np.mean(abs_diff)


def counting_problem_error_analysis2():
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
    # diagram_type = diagram_type_list[0]

    # print('%s & %s & %s & %s \\\\' % ('Diagram Type', 'Exact Match', 'Acc@1', 'Acc@2'))
    for file in log_file_dic:
        statistic_dic = generate_statistic_dic_all(file)
        result_dic = {}
        # for diagram_type in diagram_type_list:
        #     result_dic[diagram_type] =

        for diagram_type in diagram_type_list:
            mae = MAE(statistic_dic, diagram_type)
            result_dic[diagram_type] = mae
            # print('%s & %.2f & %.2f & %.2f \\\\' % (diagram_type, exact_match/total, (exact_match + pass_with_tolerance1)/total, (exact_match + pass_with_tolerance2)/total))

        print('%s & %.2f & %.2f & %.2f & %.2f \\\\' %
              (log_file_dic[file], result_dic['behavior'], result_dic['structural'], result_dic['ER'], result_dic['all']))


def directional_bias(statistic_dic, diagram_type):
    diff = []
    total = 0
    diff_positive = 0
    diff_negative = 0

    for QA_type in statistic_dic[diagram_type]:
        for x in statistic_dic[diagram_type][QA_type]:
            if check_counting_or_retrieval(QA_type) == 'counting':
                total += 1
                response_final = response_processing(x['response'])
                try:
                    response = json.loads(response_final)['answer']
                except:
                    continue
                answer = x['answer']
                diff.append(response - answer[0])
                if response - answer[0] > 0:
                    diff_positive += 1
                elif response - answer[0] < 0:
                    diff_negative += 1

    return np.mean(diff), diff_positive/total, diff_negative/total


def counting_problem_error_analysis3():
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
    # diagram_type = diagram_type_list[0]

    # print('%s & %s & %s & %s \\\\' % ('Diagram Type', 'Exact Match', 'Acc@1', 'Acc@2'))
    for file in log_file_dic:
        statistic_dic = generate_statistic_dic_all(file)
        result_dic = {}
        # for diagram_type in diagram_type_list:
        #     result_dic[diagram_type] =

        for diagram_type in diagram_type_list:
            mean_diff, positive_p, negative_p = directional_bias(statistic_dic, diagram_type)
            result_dic[diagram_type] = {
                'mean_diff': mean_diff,
                'positive_p': positive_p,
                'negative_p': negative_p,
            }
            # print('%s & %.2f & %.2f & %.2f \\\\' % (diagram_type, exact_match/total, (exact_match + pass_with_tolerance1)/total, (exact_match + pass_with_tolerance2)/total))

        print('%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\' %
              (log_file_dic[file],
               result_dic['behavior']['mean_diff'], result_dic['behavior']['positive_p'],
               result_dic['behavior']['negative_p'],
               result_dic['structural']['mean_diff'], result_dic['structural']['positive_p'],
               result_dic['structural']['negative_p'],
               result_dic['ER']['mean_diff'], result_dic['ER']['positive_p'], result_dic['ER']['negative_p'],
               result_dic['all']['mean_diff'], result_dic['all']['positive_p'], result_dic['all']['negative_p']))

log_file_dic = {
    '512/claude-sonnet-4-5_response_0213_t_0.log': 'claude-sonnet-4.5',
    '512/claude-haiku-4-5_response_0213_t_0.log': 'claude-haiku-4.5',
    # '512/claude-3-5-haiku-latest_response_0213_t_0.log': 'claude-haiku-3.5',
    '512/gemini-2.5-flash_response_0213_t_0.log': 'gemini-2.5-flash',
    '512/gemini-2.5-flash-lite_response_0213_t_0.log': 'gemini-2.5-flash-lite',
    '512/gpt-5-nano_response_0213_t_1.log': 'gpt-5-nano',
    '512/gpt-4o-mini_response_0213_t_0.log': 'gpt-4o-mini',
    '512/qwen_2.5-VL-32B_response_0213_t_0.log': 'qwen-2.5-VL-32B',
    '512/qwen_2.5-VL-7B_response_0213_t_0.log': 'qwen-2.5-VL-7B',
    '512/qwen_2.5-VL-3B_response_0213_t_0.log': 'qwen-2.5-VL-3B',
}


diagram_type_list = ["behavior", "structural", "ER", "all"]
diagram_type = diagram_type_list[3]

# for file in log_file_dic:
#     # statistic_dic = generate_statistic_dic_all(file)
#     # result_dic = {}
#     # for diagram_type in diagram_type_list:
#     #     result_dic[diagram_type] =
#
#     # for diagram_type in diagram_type_list:
#
#     statistic_table(file, diagram_type)
#     print(file)
#     a = input()
# for QA_type in statistic_dic[diagram_type]:
#     for x in statistic_dic[diagram_type][QA_type]:
#         if x['evaluation_result'] == 'False' and check_counting_or_retrieval(QA_type) == 'counting':
#             print('file', x['file'])
#             print('Question', x['question'])
#             print('=======================')
#             print('Answer', x['answer'])
#             print('Response', json.loads(response_processing(x['response']))['answer'])
#             print('=======================')
#             # json.loads(response_final)['answer']
#             a = input()

# TODO: for counting problems
#   1. exactness + tolerance: acc@+-1, acc@+-2 (Done)
#   2. magnitude of error: MAE E[|y_hat-y|] (Done)
#   3. directional bias (systematic over/under counting): r = y_hat - y; Mean Error E[r]; Overcount_rate P(r>0) / Undercount rate P(r<0)
#   Stratified analysis
#   1. By diagram type
#   2. By question subtype
#   3. By diagram complexity
#   4. By counting magnitude, e.g. 0-3, 4-7. 8-12, 13+