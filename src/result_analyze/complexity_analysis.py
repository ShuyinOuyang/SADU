import json
import os
from collections import defaultdict

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from scipy import stats
from matplotlib import colors

base_path = '../../'

EVAL_DIR = base_path + 'experiment_result/evaluation_result/512/'
JSON_OBJ_DIRS = {
    'ER': base_path + 'dataset/SAD/ER/json_object/',
    'behavior': base_path + 'dataset/SAD/behavior/json_object/',
    'structural': base_path + 'dataset/SAD/structural/json_object/',
}

MODEL_DISPLAY_NAMES = {
    'gemini-2.5-flash-lite': 'gemini-2.5-flash-lite',
    'gemini-2.5-flash': 'gemini-2.5-flash',
    'gemini-3.1-flash-lite-preview': 'gemini-3.1-flash-lite-preview',
    'gemini-3-flash-preview': 'gemini-3-flash-preview',
    'claude-haiku-4-5': 'claude-haiku-4.5',
    'claude-sonnet-4-5': 'claude-sonnet-4.5',
    'gpt-5-nano': 'gpt-5-nano',
    'gpt-4o-mini': 'gpt-4o-mini',
    'qwen_2.5-VL-32B': 'qwen-2.5-VL-32B',
    'qwen_2.5-VL-7B': 'qwen-2.5-VL-7B',
    'qwen_2.5-VL-3B': 'qwen-2.5-VL-3B',
}


# ──────────────────────────────────────────────────────────────────────────────
# 1. Load diagram sizes from JSON object files
# ──────────────────────────────────────────────────────────────────────────────

def load_diagram_sizes():
    """Return dict: (diagram_type, file_stem) -> {entities, relations, total}."""
    sizes = {}
    for dtype, dir_path in JSON_OBJ_DIRS.items():
        for fname in os.listdir(dir_path):
            if not fname.endswith('.json'):
                continue
            stem = fname[:-5]  # strip .json
            with open(os.path.join(dir_path, fname)) as f:
                obj = json.load(f)
            n_entities = len(obj.get('entity', {}))
            n_relations = len(obj.get('relation', []))
            sizes[(dtype, stem)] = {
                'entities': n_entities,
                'relations': n_relations,
                'total': n_entities + n_relations,
            }
    return sizes


# ──────────────────────────────────────────────────────────────────────────────
# 2. Load evaluation results
# ──────────────────────────────────────────────────────────────────────────────

def load_eval_results():
    """Return list of dicts, each with model, diagram_type, file, correct."""
    results = []
    for fname in sorted(os.listdir(EVAL_DIR)):
        if not fname.endswith('.log'):
            continue
        # derive model name from filename  e.g. claude-haiku-4-5_judge_0223_t_0.log
        model = fname.split('_judge_')[0]
        with open(os.path.join(EVAL_DIR, fname)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                content = json.loads(line)
                judge_line = content['judge_response'].split('\n')[0].strip().lower()
                correct = judge_line == 'true'
                ro = content['response_obj']
                results.append({
                    'model': model,
                    'diagram_type': ro['diagram_type'],
                    'file': ro['file'],
                    'correct': correct,
                })
    return results


# ──────────────────────────────────────────────────────────────────────────────
# 3. Compute per-diagram accuracy per model
# ──────────────────────────────────────────────────────────────────────────────

def compute_diagram_accuracy(results, sizes):
    """
    Returns a list of records:
      {model, diagram_type, file, entities, relations, total, accuracy, n_questions}
    One record per (model, diagram) pair.
    """
    # bucket: (model, dtype, file) -> [correct, ...]
    bucket = defaultdict(list)
    for r in results:
        key = (r['model'], r['diagram_type'], r['file'])
        bucket[key].append(r['correct'])

    records = []
    for (model, dtype, file), corrects in bucket.items():
        size_key = (dtype, file)
        if size_key not in sizes:
            continue
        sz = sizes[size_key]
        records.append({
            'model': model,
            'diagram_type': dtype,
            'file': file,
            'entities': sz['entities'],
            'relations': sz['relations'],
            'total': sz['total'],
            'accuracy': sum(corrects) / len(corrects),
            'n_questions': len(corrects),
        })
    return records


# ──────────────────────────────────────────────────────────────────────────────
# 4. Correlation analysis
# ──────────────────────────────────────────────────────────────────────────────

def correlate(x, y):
    pearson_r, pearson_p = stats.pearsonr(x, y)
    spearman_r, spearman_p = stats.spearmanr(x, y)
    return {
        'pearson_r': pearson_r,
        'pearson_p': pearson_p,
        'spearman_r': spearman_r,
        'spearman_p': spearman_p,
        'n': len(x),
    }


def run_correlation_analysis(records):
    """Compute correlations per model and overall (averaged across models)."""
    models = sorted(set(r['model'] for r in records))
    metrics = ['entities', 'relations', 'total']

    print('\n' + '=' * 80)
    print('CORRELATION: diagram size vs. accuracy')
    print('=' * 80)
    header = f"{'Model':<35} {'Metric':<12} {'Pearson r':>10} {'p-value':>10} {'Spearman r':>11} {'p-value':>10} {'N':>6}"
    print(header)
    print('-' * len(header))

    all_corr = defaultdict(list)

    for model in models:
        model_records = [r for r in records if r['model'] == model]
        for metric in metrics:
            x = np.array([r[metric] for r in model_records])
            y = np.array([r['accuracy'] for r in model_records])
            c = correlate(x, y)
            display = MODEL_DISPLAY_NAMES.get(model, model)
            print(f"{display:<35} {metric:<12} {c['pearson_r']:>10.4f} {c['pearson_p']:>10.4f} "
                  f"{c['spearman_r']:>11.4f} {c['spearman_p']:>10.4f} {c['n']:>6}")
            all_corr[metric].append(c)

    # Overall (pool all models)
    print('\n--- Overall (all models pooled) ---')
    for metric in metrics:
        x = np.array([r[metric] for r in records])
        y = np.array([r['accuracy'] for r in records])
        c = correlate(x, y)
        print(f"{'ALL MODELS':<35} {metric:<12} {c['pearson_r']:>10.4f} {c['pearson_p']:>10.4f} "
              f"{c['spearman_r']:>11.4f} {c['spearman_p']:>10.4f} {c['n']:>6}")

    # Per diagram type
    for dtype in ['ER', 'behavior', 'structural']:
        print(f'\n--- Diagram type: {dtype} (all models pooled) ---')
        dtype_records = [r for r in records if r['diagram_type'] == dtype]
        for metric in metrics:
            x = np.array([r[metric] for r in dtype_records])
            y = np.array([r['accuracy'] for r in dtype_records])
            c = correlate(x, y)
            print(f"{'ALL MODELS':<35} {metric:<12} {c['pearson_r']:>10.4f} {c['pearson_p']:>10.4f} "
                  f"{c['spearman_r']:>11.4f} {c['spearman_p']:>10.4f} {c['n']:>6}")

    return all_corr


# ──────────────────────────────────────────────────────────────────────────────
# 5. Plotting
# ──────────────────────────────────────────────────────────────────────────────

DTYPE_COLORS = {'ER': '#e41a1c', 'behavior': '#377eb8', 'structural': '#4daf4a'}


def plot_scatter_overview(records, out_path):
    """3 subplots: entities, relations, total vs accuracy (all models pooled)."""
    metrics = [('entities', 'Number of Entities'),
               ('relations', 'Number of Relations'),
               ('total', 'Total Size (Entities + Relations)')]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Diagram Size vs. Accuracy (All Models Pooled)', fontsize=13)

    for ax, (metric, xlabel) in zip(axes, metrics):
        for dtype in ['ER', 'behavior', 'structural']:
            sub = [r for r in records if r['diagram_type'] == dtype]
            x = [r[metric] for r in sub]
            y = [r['accuracy'] for r in sub]
            ax.scatter(x, y, alpha=0.4, s=20, color=DTYPE_COLORS[dtype], label=dtype)

        # fit line on all pooled
        x_all = np.array([r[metric] for r in records])
        y_all = np.array([r['accuracy'] for r in records])
        m, b = np.polyfit(x_all, y_all, 1)
        xs = np.linspace(x_all.min(), x_all.max(), 200)
        ax.plot(xs, m * xs + b, 'k--', linewidth=1.2)

        pr, pp = stats.pearsonr(x_all, y_all)
        sr, sp = stats.spearmanr(x_all, y_all)
        ax.set_xlabel(xlabel)
        ax.set_ylabel('Accuracy')
        ax.set_title(f'Pearson r={pr:.3f} (p={pp:.3f})\nSpearman r={sr:.3f} (p={sp:.3f})', fontsize=9)
        ax.legend(fontsize=7)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved overview scatter → {out_path}')
    plt.close()


def plot_per_model(records, out_path):
    """Grid of scatter plots (total size vs accuracy), one panel per model."""
    models = sorted(set(r['model'] for r in records))
    n = len(models)
    ncols = 4
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 4, nrows * 3.5))
    axes = axes.flatten()
    fig.suptitle('Total Diagram Size vs. Accuracy Per Model', fontsize=13)

    for ax, model in zip(axes, models):
        model_records = [r for r in records if r['model'] == model]
        for dtype in ['ER', 'behavior', 'structural']:
            sub = [r for r in model_records if r['diagram_type'] == dtype]
            x = [r['total'] for r in sub]
            y = [r['accuracy'] for r in sub]
            ax.scatter(x, y, alpha=0.5, s=18, color=DTYPE_COLORS[dtype], label=dtype)

        x_all = np.array([r['total'] for r in model_records])
        y_all = np.array([r['accuracy'] for r in model_records])
        if len(x_all) > 1:
            m, b = np.polyfit(x_all, y_all, 1)
            xs = np.linspace(x_all.min(), x_all.max(), 200)
            ax.plot(xs, m * xs + b, 'k--', linewidth=1.0)
            pr, _ = stats.pearsonr(x_all, y_all)
            sr, _ = stats.spearmanr(x_all, y_all)
            ax.set_title(f'{MODEL_DISPLAY_NAMES.get(model, model)}\nPearson r={pr:.3f}, Spearman r={sr:.3f}', fontsize=7.5)
        else:
            ax.set_title(MODEL_DISPLAY_NAMES.get(model, model), fontsize=8)

        ax.set_xlabel('Total Size', fontsize=8)
        ax.set_ylabel('Accuracy', fontsize=8)
        ax.legend(fontsize=6)

    for ax in axes[n:]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved per-model scatter → {out_path}')
    plt.close()


def plot_size_bins(records, out_path):
    """
    Bin diagrams by total size into quartiles and show average accuracy per bin,
    broken down by diagram type.
    """
    totals = np.array([r['total'] for r in records])
    # compute quartile boundaries on unique diagrams (not per model)
    unique_totals = np.array(list(set((r['diagram_type'], r['file'], r['total'])
                                       for r in records)))
    all_t = np.array([int(x[2]) for x in unique_totals])
    q25, q50, q75 = np.percentile(all_t, [25, 50, 75])

    def bin_label(t):
        if t <= q25:
            return f'Q1 (≤{int(q25)})'
        elif t <= q50:
            return f'Q2 ({int(q25)+1}–{int(q50)})'
        elif t <= q75:
            return f'Q3 ({int(q50)+1}–{int(q75)})'
        else:
            return f'Q4 (>{int(q75)})'

    bin_order = [f'Q1 (≤{int(q25)})', f'Q2 ({int(q25)+1}–{int(q50)})',
                 f'Q3 ({int(q50)+1}–{int(q75)})', f'Q4 (>{int(q75)})']

    dtypes = ['ER', 'behavior', 'structural', 'all']
    fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=True)
    fig.suptitle('Average Accuracy by Diagram Size Quartile', fontsize=12)

    for ax, dtype in zip(axes, dtypes):
        if dtype == 'all':
            sub = records
        else:
            sub = [r for r in records if r['diagram_type'] == dtype]

        bin_acc = defaultdict(list)
        for r in sub:
            bl = bin_label(r['total'])
            bin_acc[bl].append(r['accuracy'])

        means = [np.mean(bin_acc[b]) if bin_acc[b] else np.nan for b in bin_order]
        sems = [np.std(bin_acc[b]) / np.sqrt(len(bin_acc[b])) if bin_acc[b] else 0
                for b in bin_order]
        counts = [len(bin_acc[b]) for b in bin_order]

        bars = ax.bar(range(4), means, yerr=sems, capsize=4,
                      color=DTYPE_COLORS.get(dtype, '#999999'), alpha=0.75)
        ax.set_xticks(range(4))
        ax.set_xticklabels([f'Q{i+1}\n(n={counts[i]})' for i in range(4)], fontsize=8)
        ax.set_title(dtype, fontsize=10)
        ax.set_xlabel('Size Quartile')
        if dtype == 'ER':
            ax.set_ylabel('Mean Accuracy')
        ax.set_ylim(0, 1.05)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved quartile bar chart → {out_path}')
    plt.close()

def plot_heatmap(records, out_path, fontsize=16):
    models = [key for key in MODEL_DISPLAY_NAMES]
    totals_all = [r['total'] for r in records]
    q25, q50, q75 = np.percentile(totals_all, [25, 50, 75])

    def bin_idx(t):
        if t <= q25:
            return 0
        elif t <= q50:
            return 1
        elif t <= q75:
            return 2
        else:
            return 3

    bin_labels = [
        f'≤{int(q25)}',
        f'{int(q25)+1}–{int(q50)}',
        f'{int(q50)+1}–{int(q75)}',
        f'>{int(q75)}'
    ]

    matrix = np.full((len(models), 4), np.nan)
    for i, model in enumerate(models):
        model_recs = [r for r in records if r['model'] == model]
        bins = defaultdict(list)
        for r in model_recs:
            bins[bin_idx(r['total'])].append(r['accuracy'])
        for b, accs in bins.items():
            matrix[i, b] = np.mean(accs)

    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    cmap = colors.LinearSegmentedColormap.from_list(
        "paper_teal_light",
        [
            "#f6ddd2",
            "#ece6e2",
            "#d7ebe6",
            "#a9d3cb",
            "#5fa9a5",
        ]
    )

    im = ax.imshow(matrix, aspect='auto', vmin=0, vmax=1, cmap=cmap)

    ax.set_xticks(range(4))
    ax.set_xticklabels(bin_labels, fontsize=fontsize-2)
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels([MODEL_DISPLAY_NAMES[m] for m in models], fontsize=fontsize)
    ax.set_xlabel('Total Size (Entity Size + Relation Size)', fontsize=fontsize)

    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Accuracy', fontsize=fontsize)
    cbar.ax.tick_params(labelsize=fontsize - 1)

    for i in range(len(models)):
        for j in range(4):
            if not np.isnan(matrix[i, j]):
                val = matrix[i, j]
                ax.text(
                    j, i, f"{val:.2f}",
                    ha="center", va="center",
                    fontsize=fontsize - 1,
                    color="black"
                )

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()



# ──────────────────────────────────────────────────────────────────────────────
# 6. Size distribution summary
# ──────────────────────────────────────────────────────────────────────────────

def print_size_summary(sizes):
    print('\n' + '=' * 60)
    print('DIAGRAM SIZE DISTRIBUTION')
    print('=' * 60)
    for dtype in ['ER', 'behavior', 'structural']:
        sub = {k: v for k, v in sizes.items() if k[0] == dtype}
        ents = [v['entities'] for v in sub.values()]
        rels = [v['relations'] for v in sub.values()]
        tots = [v['total'] for v in sub.values()]
        print(f'\n{dtype} ({len(sub)} diagrams)')
        print(f"  Entities  : min={min(ents)}, max={max(ents)}, mean={np.mean(ents):.1f}, median={np.median(ents):.1f}")
        print(f"  Relations : min={min(rels)}, max={max(rels)}, mean={np.mean(rels):.1f}, median={np.median(rels):.1f}")
        print(f"  Total     : min={min(tots)}, max={max(tots)}, mean={np.mean(tots):.1f}, median={np.median(tots):.1f}")


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

# def main():
out_dir = base_path + 'experiment_result/analysis_result/'
os.makedirs(out_dir, exist_ok=True)

print('Loading diagram sizes...')
sizes = load_diagram_sizes()
print(f'  Loaded {len(sizes)} diagrams')
print_size_summary(sizes)

print('\nLoading evaluation results...')
results = load_eval_results()
print(f'  Loaded {len(results)} evaluation entries')

print('\nComputing per-diagram accuracy...')
records = compute_diagram_accuracy(results, sizes)
print(f'  {len(records)} (model, diagram) pairs')

# run_correlation_analysis(records)

print('\nGenerating plots...')
# plot_scatter_overview(records, out_dir + 'complexity_scatter_overview.pdf')
# plot_per_model(records, out_dir + 'complexity_scatter_per_model.pdf')
# plot_size_bins(records, out_dir + 'complexity_quartile_bars.pdf')
plot_heatmap(records, out_dir + 'complexity_heatmap.pdf')

print('\nDone.')
