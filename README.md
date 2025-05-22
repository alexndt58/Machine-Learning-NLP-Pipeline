# Real-Time Twitter Topic Classification  
*CETM47 AS2 | MSc Data Science*

**Author:** Ayodeji Jayeoba   
**Module:** CETM47: Machine Learning & NLP  
**Repository:** [GitHub URL: https://github.com/alexndt58/Machine-Learning-NLP-Pipeline.git]


##  Project Overview

This repository contains a fully reproducible, end-to-end NLP pipeline for **real-time classification of tweets into editorial topics**.  
The solution is tailored for NewsPulse Analytics—a scenario where editors must triage breaking stories from thousands of tweets per hour, with a target latency ≤ 0.5s and macro-F1 ≥ 0.85.

**Key Features:**
- Modular, YAML-driven preprocessing and vectorization
- Char-TFIDF, word-TFIDF, GloVe, and SBERT representations
- Hyper-parameter optimized experiments, tracked in MLflow
- Robust evaluation: stratified splits, nested cross-validation, statistical testing
- Full documentation and figures for each project step

---

## 📁 Project Structure

Machine-Learning-NLP-Pipeline/
├── src/ # Core pipeline code and models
├── flows/ # Experiment orchestration scripts
├── conf/ # YAML configs for pipeline/experiments
├── notebooks/ # EDA and evaluation notebooks
├── reports/figures/ # All output plots and figures
├── data/raw/ # Raw JSON data (do not share publicly)
├── data/splits/ # Pre-defined train/val/test splits
├── tests/ # Unit tests
├── docs/ # Report markdown sections
├── requirements.txt # Python dependencies
└── README.md


---

## Getting Started

### 1. **Clone or extract the repository**

```bash
git clone <repo-url>
cd Machine-Learning-NLP-Pipeline
or unpack the ZIP and open in VS Code.


### 2. Set up your Python environment

python -m venv .venv
# Activate (Windows):
.venv\Scripts\activate
# Activate (Mac/Linux):
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt


### 3. Run EDA and Data Preparation

jupyter notebook notebooks/01_eda.ipynb

Generates EDA plots in reports/figures/

Saves cleaned data to data/tweets.feather


### 4. Run Experiments

python flows/experiment_grid.py

Performs model grid search using configs in conf/
Logs results to MLflow (optional: run mlflow ui to inspect)

### 5. Aggregate Results & Visualize

python src/gather_results.py
jupyter notebook notebooks/04_eval.ipynb

### 6. Run Tests

pytest -q

## Results Snapshot

Best Model: Char-TFIDF + Linear SVM

Macro-F1: 0.864 Latency: 280ms (median, CPU)

Key Figures: See reports/figures/ for class distribution, confusion matrix, and ROC curves

Business Impact: Estimated >6 analyst-hours/day saved; robust to concept drift (PSI monitored)

## Reproducibility & Notes

All splits, configs, and random seeds are pre-versioned.

No raw virtual environments or large binaries in repo—see requirements.txt for dependencies.

All code and results are organized per CRISP-DM and KDD best practice.

## References

Chapman, P. et al. (2000). CRISP-DM 1.0: Step-by-Step Data Mining Guide

Rizwan, M. et al. (2023). Char-level n-grams outperform BERT for noisy social text. ACL SRW.

Pennington, J. et al. (2014). GloVe: Global Vectors for Word Representation. EMNLP.

Reimers, N. & Gurevych, I. (2021). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP.

[Additional references in docs/ and project report]