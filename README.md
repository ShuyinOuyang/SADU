# SADU: A Benchmark for Software Architecture Diagram Understanding

Official repository for **SADU**, a benchmark for evaluating multimodal models on **software architecture diagram understanding**.

SADU focuses on question answering over software-engineering diagrams, with an emphasis on diagram reasoning tasks such as **counting** and **retrieval**. The repository includes benchmark data, model response generation scripts, evaluation code, and result-analysis utilities.

---

## 👋 Overview

Software architecture diagrams are widely used to communicate system structure and behavior, but they remain challenging inputs for modern vision-language models. SADU is designed to support systematic evaluation of this problem by organizing diagram samples, question-answer pairs, model outputs, and analysis scripts in a reproducible benchmark pipeline.

At a high level, this repository supports four stages:

1. **Benchmark construction**: convert and process diagram sources, generate QA pairs, and perform format checks.
2. **Model inference**: run different multimodal models to generate responses on the benchmark.
3. **Evaluation**: score responses with rule-based and LLM-based evaluators.
4. **Result analysis**: study aggregate performance and error patterns for counting and retrieval tasks.

---

## 💻 Repository Structure

```text
SADU/
├── dataset/
│   └── SAD/
│       ├── behavior/
│       ├── structural/
│       └── ER/
│   └── SAD_hard/
│       ├── long_arrow/
│       ├── multiple_arrow/
│       └── not_right_arrow/
│       └── overlap_arrow/
├── experiment_result/
│   ├── evaluation_result/
│   └── response_result/
├── src/
│   ├── benchmark_construction/
│   ├── evaluation/
│   ├── generation/
│   └── result_analyze/
└── personal_token/
```

### `dataset/SAD/`
The SADU benchmark can be downloaded from [here](/dataset/SAD).
Benchmark data grouped by diagram type:
- `behavior/`
- `structural/`
- `ER/`

### `src/benchmark_construction/`
Utilities for building and processing the benchmark, including scripts for:
- diagram extraction and conversion,
- SVG/UXF processing,
- QA generation,
- hard-example generation,
- and format checking.

### `src/generation/`
Inference scripts for collecting model responses from multiple model families, including:
- GPT,
- Gemini,
- Claude,
- Qwen.

### `src/evaluation/`
Evaluation scripts for two complementary settings:
- **rule-based evaluation**
- **LLM-based evaluation**

### `src/result_analyze/`
Analysis scripts for reporting benchmark statistics and studying failure modes, including:
- counting error analysis,
- retrieval error analysis,
- result display,
- summary statistics.

### `experiment_result/`
Stores experiment outputs, including raw model responses and evaluated results.

---

## 💽Benchmark Scope

SADU is intended for evaluating how well multimodal models understand software-engineering diagrams rather than only reading text from images. The benchmark is organized around multiple diagram categories and supports reasoning-heavy question types such as:

- **Counting**: e.g., number of entities, components, or relations.
- **Retrieval**: e.g., identifying connected elements, sources, targets, or sets of relevant entities.

This setup makes the benchmark suitable for studying both **diagram perception** and **structural reasoning**.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ShuyinOuyang/SADU.git
cd SADU
```

### 2. Create a Python environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
```

### 3. Install dependencies

Because the repository currently does not expose an installation manifest in the visible top-level structure, install the packages required by the scripts you plan to run.
A practical starting point is:

```bash
pip install openai anthropic google-generativeai pandas numpy matplotlib tqdm pillow
```

You may need additional packages depending on the benchmark-construction pipeline and the model backend you use.

---

## 💫 Usage

### Benchmark construction

Scripts under `src/benchmark_construction/` support preprocessing and benchmark creation.
Typical tasks include:

- extracting diagram content from source files,
- converting diagrams into intermediate JSON-like representations,
- generating question-answer pairs,
- validating output formats.

Example:

```bash
python src/benchmark_construction/generate_QA.py
```

### Generate model responses

Use the scripts in `src/generation/` to run supported models on the benchmark.

Examples:

```bash
python src/generation/gpt_generate_response.py
python src/generation/gemini_generate_response.py
python src/generation/claude_generate_response.py
python src/generation/qwen_generate_response.py
```

These scripts are expected to save raw outputs to `experiment_result/response_result/`.

### Evaluate responses

Run either rule-based or LLM-based evaluation depending on your setup.

```bash
python evaluation_rule_based.py -t "target_file_path" &> "log_file_path" &
python evaluation_llm_based.py -t "target_file_path" -l "judge.log" &> "log_file_path" &
```

Evaluated outputs can then be stored under `experiment_result/evaluation_result/`.

### Analyze results

Use the analysis scripts to summarize performance and inspect failure cases.

```bash
python src/result_analyze/statistic_display.py
python src/result_analyze/result_display.py
python src/result_analyze/counting_error_analysis.py
python src/result_analyze/retrieval_error_analysis.py
```

---

## 📍 Expected Workflow

A typical end-to-end workflow is:

1. Prepare or inspect diagrams in `dataset/SAD/`.
2. Generate or verify QA pairs with the benchmark-construction scripts.
3. Run multimodal models to collect responses.
4. Evaluate responses with rule-based and/or LLM-based judges.
5. Analyze performance by diagram type and question type.

---

## Reproducibility Notes

- Store API keys or private credentials outside the repository when possible.
- Keep raw responses and evaluated outputs in separate folders for traceability.
- When reporting numbers in a paper, specify:
  - model version,
  - prompting strategy,
  - evaluation setting,
  - subset used (`behavior`, `structural`, `ER`),
  - and whether metrics come from rule-based or judge-based scoring.

---

## 📜 Acknowledgement

This repository supports research on multimodal reasoning for software engineering artifacts, with a focus on software architecture diagram understanding.

---

## ✍️ Contact

For questions, please open an issue in the repository or contact the repository maintainers through GitHub.
