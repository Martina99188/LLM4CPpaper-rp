# LLM4CPpaper-rp

Replication package for the paper:

**A Study on Leveraging Large Language Models for Category-Partition Testing**

---

## 🔗 Zenodo Dataset

The experimental dataset is available at:

[Replication Package: A Study on Leveraging Large Language Models for Category-Partition Testing](https://doi.org/10.5281/zenodo.20141514)

---

## 📌 Description

This replication package provides the artifacts and scripts required to reproduce the empirical evaluation of LLMs for Category-Partition Method (CPM)-based test generation.

The study investigates the ability of large language models to generate structured test artifacts from natural language functional specifications, and compares multiple models under a controlled evaluation framework.

The repository includes:
- Prompt templates used for CPM-based test generation
- LLM-generated outputs (ChatGPT, Gemini, DeepSeek)
- Evaluation scripts and visualization tools for result analysis

---

## 📁 Repository Structure

### 1. Python Project (`src/`)
This folder contains scripts for evaluating and visualizing experimental results:
- `BarChart.py`: compares average performance of LLMs (ChatGPT, Gemini, DeepSeek) across evaluation criteria
- `HeatMapChatGPT.py`: generates heatmap-based analysis of ChatGPT results
- `HeatMapGemini.py`: generates heatmap-based analysis of Gemini results
- `HeatMapDeepSeek.py`: generates heatmap-based analysis of DeepSeek results
- `LinePlot.py`: visualizes trends and variations across evaluation dimensions

---

### 2. Inputs (`inputs/`)
This folder contains the input artifacts used in the experimental pipeline:
- `requirements_full.csv`: complete set of functional requirements describing the e-learning platform
- `requirements_eval.csv`: subset of representative requirements used for qualitative evaluation
- `use_case_description.txt`: description of the e-learning system, including user roles and functional behavior

---

### 3. Prompts (`prompts/`)
This folder contains the prompt template used for CPM-based test generation:
- `cp_prompt.txt`: unified prompt used to extract Category-Partition structures (parameters, categories, and choices) from functional specifications

---

### 4. Data (`data/`)
This folder contains all experimental outputs and evaluation artifacts:

- `evaluation/`: visual results including bar charts, heatmaps, and line plots comparing LLM performance
- `results_chatgpt/`: CPM structures and generated test cases produced by ChatGPT
- `results_gemini/`: CPM structures and generated test cases produced by Gemini
- `results_deepseek/`: CPM structures and generated test cases produced by DeepSeek

---

## 🧪 Experimental Subject

The experimental evaluation is conducted on a simulated e-learning platform defined through a set of functional requirements.

The system models key functionalities such as user registration, course management, class scheduling, and synchronous interaction between teachers and students.

These requirements serve as the basis for evaluating the ability of LLMs to generate structured CPM-based test artifacts from natural language specifications.

---

## ▶️ Replication Procedure

To reproduce the experimental analysis, follow these steps:

1. Ensure all required Python dependencies are installed (e.g., matplotlib, numpy, pandas).

2. Run the evaluation and visualization scripts:
```bash
python src/BarChart.py
python src/HeatMapChatGPT.py
python src/HeatMapGemini.py
python src/HeatMapDeepSeek.py
python src/LinePlot.py
```
3. Generated plots will be stored in the data/evaluation/ directory.

---

```md
## 👤 Contact

Corresponding author: AnonymousAuthor1Name AnonymousAuthor1Surname  
Email: AnonymousAuthor1Mail
```

---

## 📚 Citing this work

If you use this replication package, please cite:

@inproceedings{LLM4CP,
  author    = {AnonymousAuthor1Name and AnonymousAuthor2Name},
  title     = {A Study on Leveraging Large Language Models for Category-Partition Testing},
  booktitle = {TO BE UPDATED AFTER ACCEPTANCE},
  year      = {2026}
}

## ⚠️ Notes

This repository is anonymized for peer review.

All identifiers will be updated after acceptance.

LLM outputs may vary due to model non-determinism.
