import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from util import *


diagram_type_list = ["behavior", "structural", "ER", "all"]
diagram_type = diagram_type_list[3]


def llm_based_eval_display(file_list, file):
    res_list = []
    with open(base_path + 'experiment_result/evaluation_result/' + file, 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            judge = content['judge_response'].split('\n')[0].strip()
            if judge.lower() == 'true':
                content['judge'] = 'True'
            elif judge.lower() == 'false':
                content['judge'] = 'False'
            else:
                content['judge'] = 'Not Valid'

            res_list.append(content)

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

    for content in res_list:
        statistic_dict[content['response_obj']['diagram_type']][content['response_obj']['metadata']['sub_type']].append(content['judge'])
        statistic_dict['all'][content['response_obj']['metadata']['sub_type']].append(content['judge'])

    # print total
    sum_total_bahavior = sum([len(statistic_dict['behavior'][QA_sub_type]) for QA_sub_type in statistic_dict['behavior']])
    sum_true_bahavior = sum([statistic_dict['behavior'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['behavior']])

    sum_total_structural = sum([len(statistic_dict['structural'][QA_sub_type]) for QA_sub_type in statistic_dict['structural']])
    sum_true_structural = sum([statistic_dict['structural'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['structural']])

    sum_total_ER = sum([len(statistic_dict['ER'][QA_sub_type]) for QA_sub_type in statistic_dict['ER']])
    sum_true_ER = sum([statistic_dict['ER'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['ER']])

    sum_total_all = sum([len(statistic_dict['all'][QA_sub_type]) for QA_sub_type in statistic_dict['all']])
    sum_true_all = sum([statistic_dict['all'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['all']])

    # sum_false = sum([statistic_dict[diagram_type][QA_sub_type].count('False') for QA_sub_type in statistic_dict[diagram_type]])
    # sum_error = sum([statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type]])

    print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' %
          (file_list[file],
           # sum_total,
           # sum_true,
           sum_true_bahavior/sum_total_bahavior * 100,
           sum_true_structural / sum_total_structural * 100,
           sum_true_ER / sum_total_ER * 100,
           sum_true_all / sum_total_all * 100,
           ))

def get_llm_based_eval_display(file):
    res_list = []
    with open(base_path + 'experiment_result/evaluation_result/' + file, 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            judge = content['judge_response'].split('\n')[0].strip()
            if judge.lower() == 'true':
                content['judge'] = 'True'
            elif judge.lower() == 'false':
                content['judge'] = 'False'
            else:
                content['judge'] = 'Not Valid'

            res_list.append(content)

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

    for content in res_list:
        statistic_dict[content['response_obj']['diagram_type']][content['response_obj']['metadata']['sub_type']].append(
            content['judge'])
        statistic_dict['all'][content['response_obj']['metadata']['sub_type']].append(content['judge'])

    # print total
    # sum_total_bahavior = sum(
    #     [len(statistic_dict['behavior'][QA_sub_type]) for QA_sub_type in statistic_dict['behavior']])
    # sum_true_bahavior = sum(
    #     [statistic_dict['behavior'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['behavior']])
    #
    # sum_total_structural = sum(
    #     [len(statistic_dict['structural'][QA_sub_type]) for QA_sub_type in statistic_dict['structural']])
    # sum_true_structural = sum(
    #     [statistic_dict['structural'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['structural']])
    #
    # sum_total_ER = sum([len(statistic_dict['ER'][QA_sub_type]) for QA_sub_type in statistic_dict['ER']])
    # sum_true_ER = sum([statistic_dict['ER'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['ER']])
    #
    # sum_total_all = sum([len(statistic_dict['all'][QA_sub_type]) for QA_sub_type in statistic_dict['all']])
    # sum_true_all = sum([statistic_dict['all'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['all']])


    return statistic_dict

def RQ1_accuracy():
    model_list = {
        '512/gemini-2.5-flash-lite_judge_0223_t_0.log': 'gemini-2.5-flash-lite',
        '512/gemini-2.5-flash_judge_0223_t_0.log': 'gemini-2.5-flash',
        '512/gemini-3.1-flash-lite-preview_judge_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
        '512/gemini-3-flash-preview_judge_0223_t_0.log': 'gemini-3-flash-preview',

        '512/claude-haiku-4-5_judge_0223_t_0.log': 'claude-haiku-4.5',
        '512/claude-sonnet-4-5_judge_0223_t_0.log': 'claude-sonnet-4.5',

        '512/gpt-5-nano_judge_0223_t_1.log': 'gpt-5-nano',
        '512/gpt-4o-mini_judge_0223_t_0.log': 'gpt-4o-mini',

        '512/qwen_2.5-VL-32B_judge_0223_t_0.log': 'qwen-2.5-VL-32B',
        '512/qwen_2.5-VL-7B_judge_0223_t_0.log': 'qwen-2.5-VL-7B',
        '512/qwen_2.5-VL-3B_judge_0223_t_0.log': 'qwen-2.5-VL-3B'
    }
    for file in model_list:
        llm_based_eval_display(model_list, file)

def RQ1_cost_display():
    # diagram_type_list = ["behavior", "structural", "ER", "all"]
    # diagram_type = diagram_type_list[0]
    # file = '512/gpt-4o-mini_response_0213_t_0.log'

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
    for file in log_file_dic:
        # print(file)
        QA_response_list = []
        with open(base_path + 'experiment_result/response_result/%s' % (file), 'r') as f:
            for line in f.readlines():
                content = json.loads(line)
                QA_response_list.append(content)

        statistic_dict = {
            'behavior': {
                'completion_tokens_list': [],
                'prompt_tokens_list': [],
            },
            'structural': {
                'completion_tokens_list': [],
                'prompt_tokens_list': [],
            },
            'ER': {
                'completion_tokens_list': [],
                'prompt_tokens_list': [],
            },
            'all': {
                'completion_tokens_list': [],
                'prompt_tokens_list': [],
            }
        }

        sub_types = load_sub_types()
        for x in sub_types:
            for key in statistic_dict:
                statistic_dict[key][x] = []


        for QA_response in QA_response_list:
            token_usage = QA_response["token_usage"]
            completion_tokens = token_usage["completion_tokens"]
            prompt_tokens = token_usage["prompt_tokens"]
            if 'thoughts_token' in token_usage and token_usage["thoughts_token"]:
                statistic_dict[QA_response['diagram_type']]['completion_tokens_list'].append(completion_tokens + token_usage["thoughts_token"])
                statistic_dict[QA_response['diagram_type']]['prompt_tokens_list'].append(prompt_tokens)

                statistic_dict['all']['completion_tokens_list'].append(completion_tokens + token_usage["thoughts_token"])
                statistic_dict['all']['prompt_tokens_list'].append(prompt_tokens)
            else:
                statistic_dict[QA_response['diagram_type']]['completion_tokens_list'].append(completion_tokens)
                statistic_dict[QA_response['diagram_type']]['prompt_tokens_list'].append(prompt_tokens)

                statistic_dict['all']['completion_tokens_list'].append(completion_tokens)
                statistic_dict['all']['prompt_tokens_list'].append(prompt_tokens)

        print('%s & %.2f & %.2f & %.2f & %.2f \\\\' %
              (log_file_dic[file],
               np.mean(statistic_dict['behavior']['completion_tokens_list']),
               np.mean(statistic_dict['structural']['completion_tokens_list']),
               np.mean(statistic_dict['ER']['completion_tokens_list']),
               np.mean(statistic_dict['all']['completion_tokens_list'])
               ))

def RQ3_prompt_engineering():
    prompt_engineering_file_list = {
        'different_prompt/gemini-2.5-flash-lite_judge_0223_t_0.log': 'full & gemini-2.5-flash-lite',
        'different_prompt/gemini-2.5-flash_judge_0223_t_0.log': 'full & gemini-2.5-flash',
        'different_prompt/gemini-3.1-flash-lite-preview_judge_0223_t_0.log': 'full & gemini-3.1-flash-lite-preview',
        'different_prompt/gemini-3-flash-preview_judge_0223_t_0.log': 'full & gemini-3-flash-preview',

        'different_prompt/without_definition_gemini-2.5-flash-lite_judge_0306_t_0.log': 'without definition & gemini-2.5-flash-lite',
        'different_prompt/without_definition_gemini-2.5-flash_judge_0306_t_0.log': 'without definition & gemini-2.5-flash',
        'different_prompt/without_definition_gemini-3.1-flash-lite-preview_judge_0306_t_0.log': 'without definition & gemini-3.1-flash-lite-preview',
        'different_prompt/without_definition_gemini-3-flash-preview_judge_0306_t_0.log': 'without definition & gemini-3-flash-preview',

        'different_prompt/without_rules_gemini-2.5-flash-lite_judge_0306_t_0.log': 'without rules & gemini-2.5-flash-lite',
        'different_prompt/without_rules_gemini-2.5-flash_judge_0306_t_0.log': 'without rules & gemini-2.5-flash',
        'different_prompt/without_rules_gemini-3.1-flash-lite-preview_judge_0306_t_0.log': 'without rules & gemini-3.1-flash-lite-preview',
        'different_prompt/without_rules_gemini-3-flash-preview_judge_0306_t_0.log': 'without rules & gemini-3-flash-preview',

        'different_prompt/only_question_gemini-2.5-flash-lite_judge_0306_t_0.log': 'only question & gemini-2.5-flash-lite',
        'different_prompt/only_question_gemini-2.5-flash_judge_0306_t_0.log': 'only question & gemini-2.5-flash',
        'different_prompt/only_question_gemini-3.1-flash-lite-preview_judge_0306_t_0.log': 'only question & gemini-3.1-flash-lite-preview',
        'different_prompt/only_question_gemini-3-flash-preview_judge_0306_t_0.log': 'only question & gemini-3-flash-preview',
    }
    for file in prompt_engineering_file_list:
        llm_based_eval_display(prompt_engineering_file_list, file)

def RQ4_thinking_level():
    prompt_engineering_file_list = {
        'thinking_level/gemini-3-flash-preview_judge_0223_t_0.log': 'default & full',
        'thinking_level/only_question_gemini-3-flash-preview_judge_0223_t_0.log': 'default & only question',
        'thinking_level/low_gemini-3-flash-preview_judge_0223_t_0.log': 'low & full',
        'thinking_level/low_only_question_gemini-3-flash-preview_judge_0223_t_0.log': 'low & only question',
        'thinking_level/high_gemini-3-flash-preview_judge_0223_t_0.log': 'high & full',
        'thinking_level/high_only_question_gemini-3-flash-preview_judge_0223_t_0.log': 'high & only question',
    }
    for file in prompt_engineering_file_list:
        llm_based_eval_display(prompt_engineering_file_list, file)

def get_subtype_res(file):
    res_list = []
    with open(base_path + 'experiment_result/evaluation_result/' + file, 'r') as f:
        for line in f.readlines():
            content = json.loads(line)
            judge = content['judge_response'].split('\n')[0].strip()
            if judge.lower() == 'true':
                content['judge'] = 'True'
            elif judge.lower() == 'false':
                content['judge'] = 'False'
            else:
                content['judge'] = 'Not Valid'

            res_list.append(content)

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

    res = {}
    for content in res_list:
        statistic_dict[content['response_obj']['diagram_type']][content['response_obj']['metadata']['sub_type']].append(
            content['judge'])
        statistic_dict['all'][content['response_obj']['metadata']['sub_type']].append(content['judge'])

    # sum_total_bahavior = sum([len(statistic_dict['behavior'][QA_sub_type]) for QA_sub_type in statistic_dict['behavior']])
    # sum_true_bahavior = sum([statistic_dict['behavior'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['behavior']])
    #
    # sum_total_structural = sum([len(statistic_dict['structural'][QA_sub_type]) for QA_sub_type in statistic_dict['structural']])
    # sum_true_structural = sum([statistic_dict['structural'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['structural']])
    #
    # sum_total_ER = sum([len(statistic_dict['ER'][QA_sub_type]) for QA_sub_type in statistic_dict['ER']])
    # sum_true_ER = sum([statistic_dict['ER'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['ER']])
    #
    # sum_total_all = sum([len(statistic_dict['all'][QA_sub_type]) for QA_sub_type in statistic_dict['all']])
    # sum_true_all = sum([statistic_dict['all'][QA_sub_type].count('True') for QA_sub_type in statistic_dict['all']])

    # sum_false = sum([statistic_dict[diagram_type][QA_sub_type].count('False') for QA_sub_type in statistic_dict[diagram_type]])
    # sum_error = sum([statistic_dict[diagram_type][QA_sub_type].count('Parse Error') for QA_sub_type in statistic_dict[diagram_type]])

    for sub_type in statistic_dict['all']:
        sum_true = statistic_dict['all'][sub_type].count('True')
        sum_total = len(statistic_dict['all'][sub_type])

        if sum_total == 0:
            res[sub_type] = 0
        else:
            res[sub_type] = sum_true/sum_total
        # }
        #     'sum_true': sum_true,
        #     'sum_total': sum_total,
        # }

    return res

def draw_one_plot(file_dic, res_list, target_kind, figsize=(16, 7.5), fontsize=30, save=False):
    color_palette = [
        "#006d77",
        "#83c5be",
        "#edf6f9",
        "#ffddd2",
    ]

    subtypes = [
        s for s in res_list[0].keys()
        if check_counting_or_retrieval(s) == target_kind
    ]

    if not subtypes:
        print(f"No subtypes found for {target_kind}")
        return

    q_labels = [f"q{i+1}" for i in range(len(subtypes))]

    x = np.arange(len(subtypes))
    width = 0.78 / len(file_dic)

    fig = plt.figure(figsize=figsize)
    if target_kind == 'counting':
        gs = GridSpec(
            2, 1,
            height_ratios=[0.18, 0.82],
            hspace=0.05,
            figure=fig
        )

        ax_legend = fig.add_subplot(gs[0])
        ax = fig.add_subplot(gs[1])
    else:
        gs = GridSpec(
            2, 1,
            height_ratios=[0.01, 0.99],
            hspace=0.05,
            figure=fig
        )

        ax_legend = fig.add_subplot(gs[0])
        ax = fig.add_subplot(gs[1])
    ax_legend.axis("off")

    handles = []
    labels = []

    for i, file in enumerate(file_dic):
        values = [res_list[i].get(subtype, 0) for subtype in subtypes]
        color = color_palette[i % len(color_palette)]

        bars = ax.bar(
            x + i * width,
            values,
            width=width,
            label=str(file),
            color=color,
            edgecolor="black",
            linewidth=1.0,
        )
        handles.append(bars[0])
        labels.append(file_dic[file])

    ax.set_xticks(x + width * (len(file_dic) - 1) / 2)
    ax.set_xticklabels(q_labels, fontsize=fontsize - 2)
    ax.set_ylabel("Accuracy", fontsize=fontsize)
    ax.set_ylim(0, 1.01)

    ax.tick_params(axis="y", labelsize=fontsize - 2)
    ax.tick_params(axis="x", labelsize=fontsize - 2, pad=8)

    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
    if target_kind == 'counting':
        ax_legend.legend(
            handles,
            labels,
            loc="center",
            bbox_to_anchor=(0.47, 0.5),
            ncol=min(len(file_dic), 2),
            fontsize=fontsize - 2,
            frameon=True,
            columnspacing=1.4,
            handletextpad=0.7,
            borderpad=0.5,
        )

    fig.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.12)

    if save:
        plt.savefig(f"../../fig/{target_kind}_subtype_fig.pdf", bbox_inches="tight")
    else:
        plt.show()

def draw_plot(file_dic, save):
    res_list = []
    for file in file_dic:
        res_list.append(get_subtype_res(file))

    draw_one_plot(file_dic, res_list, "counting", save=save)
    draw_one_plot(file_dic, res_list, "retrieval", save=save)


def RQ1_subtype_plot_display():
    # file = '512/gemini-3-flash-preview_judge_0223_t_0.log'
    file_dic = {
        # '512/gemini-2.5-flash-lite_judge_0223_t_0.log': 'gemini-2.5-flash-lite',
        # '512/gemini-2.5-flash_judge_0223_t_0.log': 'gemini-2.5-flash',
        # '512/gemini-3.1-flash-lite-preview_judge_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
        '512/gemini-3-flash-preview_judge_0223_t_0.log': 'gemini-3-flash-preview',

        # '512/claude-haiku-4-5_judge_0223_t_0.log': 'claude-haiku-4.5',
        '512/claude-sonnet-4-5_judge_0223_t_0.log': 'claude-sonnet-4.5',
        #
        '512/gpt-5-nano_judge_0223_t_1.log': 'gpt-5-nano',
        # '512/gpt-4o-mini_judge_0223_t_0.log': 'gpt-4o-mini',
        #
        '512/qwen_2.5-VL-32B_judge_0223_t_0.log': 'qwen-2.5-VL-32B',
        # '512/qwen_2.5-VL-7B_judge_0223_t_0.log': 'qwen-2.5-VL-7B',
        # '512/qwen_2.5-VL-3B_judge_0223_t_0.log': 'qwen-2.5-VL-3B'
    }
    draw_plot(file_dic, save=True)


def compare_boolean_dict_lists(list1, list2):
    all_results = []

    for d1, d2 in zip(list1, list2):
        res = {}
        overall = {
            "true_same": 0,
            "false_same": 0,
            "true_different": 0,
            "false_different": 0,
        }

        common_keys = set(d1.keys()) & set(d2.keys())

        for key in common_keys:
            stats = {
                "true_same": 0,
                "false_same": 0,
                "true_different": 0,
                "false_different": 0,
            }

            v1 = d1[key]
            v2 = d2[key]
            # min_len = min(len(v1), len(v2))

            for a, b in zip(v1, v2):
                if a == b:
                    if a == 'True':
                        stats["true_same"] += 1
                    else:
                        stats["false_same"] += 1
                else:
                    if a == 'True':
                        stats["true_different"] += 1
                    else:
                        stats["false_different"] += 1

            # for a in v1[min_len:]:
            #     if a == 'True':
            #         stats["true_different"] += 1
            #     else:
            #         stats["false_different"] += 1
            #
            # for b in v2[min_len:]:
            #     if b:
            #         stats["false_different"] += 1
            #     else:
            #         stats["true_different"] += 1

            res[key] = stats

            for k in overall:
                overall[k] += stats[k]

        res["overall"] = overall
        all_results.append(res)

    return all_results


def RQ5_llm_judge_rule_based_judge():
    llm_judge_list = {
        '512/gemini-2.5-flash-lite_judge_0223_t_0.log': 'gemini-2.5-flash-lite',
        '512/gemini-2.5-flash_judge_0223_t_0.log': 'gemini-2.5-flash',
        '512/gemini-3.1-flash-lite-preview_judge_0223_t_0.log': 'gemini-3.1-flash-lite-preview',
        '512/gemini-3-flash-preview_judge_0223_t_0.log': 'gemini-3-flash-preview',

        '512/claude-haiku-4-5_judge_0223_t_0.log': 'claude-haiku-4.5',
        '512/claude-sonnet-4-5_judge_0223_t_0.log': 'claude-sonnet-4.5',

        '512/gpt-5-nano_judge_0223_t_1.log': 'gpt-5-nano',
        '512/gpt-4o-mini_judge_0223_t_0.log': 'gpt-4o-mini',

        '512/qwen_2.5-VL-32B_judge_0223_t_0.log': 'qwen-2.5-VL-32B',
        '512/qwen_2.5-VL-7B_judge_0223_t_0.log': 'qwen-2.5-VL-7B',
        '512/qwen_2.5-VL-3B_judge_0223_t_0.log': 'qwen-2.5-VL-3B'
    }

    rule_based_judge_list = {
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

    llm_judge_res_list = []
    file_list = []
    for file in llm_judge_list:
        res = get_llm_based_eval_display(file)
        llm_judge_res_list.append(res['all'])
        file_list.append(llm_judge_list[file])

    rule_based_res_list = []
    for file in rule_based_judge_list:
        res = statistic_table(file)
        rule_based_res_list.append(res['all'])

    a = compare_boolean_dict_lists(llm_judge_res_list, rule_based_res_list)

    res_dic = {}
    for i in range(len(file_list)):
        res_dic[file_list[i]] = a[i]
    sum_total = sum([len(llm_judge_res_list[0][x]) for x in llm_judge_res_list[0]])
    for file in res_dic:
        res = res_dic[file]['overall']
        print('%s & %.2f\%% & %.2f\%% & %.2f\%% & %.2f\%% \\\\' % (
            file,
            res['true_same']/sum_total * 100,
            res['false_same'] / sum_total * 100,
            res['true_different'] / sum_total * 100,
            res['false_different'] / sum_total * 100
        ))


def print_caption_RQ2():
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

    for i in range(len(counting_types)):
        print('q%s: %s;' % (i+1, counting_types[i].replace('_', ' ')))

    for i in range(len(retrieval_types)):
        print('q%s: %s;' % (i+1, retrieval_types[i].replace('_', ' ')))