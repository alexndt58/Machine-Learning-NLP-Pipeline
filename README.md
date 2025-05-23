# Real-Time Twitter Topic Classification  
*CETM47 AS2 | MSc Data Science*

**Author:** Ayodeji Jayeoba   
**Module:** CETM47: Machine Learning & NLP  
**Repository:** [GitHub URL: https://github.com/alexndt58/Machine-Learning-NLP-Pipeline.git]


##  Project Overview

This repository contains a fully reproducible, end-to-end NLP pipeline for **real-time classification of tweets into editorial topics**.  
The solution is tailored for NewsPulse Analytics—a scenario where editors must triage breaking stories from thousands of tweets per hour, with a target latency ≤ 0.5s and macro-F1 ≥ 0.85.


## 📁 Project Structure

Machine-Learning-NLP-Pipeline/
├── README.md                # Main project instructions
├── requirements.txt         # Python dependencies
├── conf/
│   ├── rep_word_tfidf.yaml
│   ├── rep_chargram.yaml
│   └── ... (more configs)
├── src/
│   ├── run_eda.py
│   ├── run_experiment.py
│   ├── gather_results.py
│   └── ... (other .py scripts)
├── flows/
│   └── experiment_grid.py
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 04_eval.ipynb
├── reports/
│   ├── results_table2.csv
│   ├── best_model_predictions.csv
│   └── figures/
│       ├── cm_best.png
│       └── ... (other images)
├── data/
│   ├── tweets.feather
│   └── ... (other processed data)
├── data/raw/
│   └── CETM47_24_5-AS2-Data.json
└── tests/
    └── test_clean.py


```YAML
## Getting Started

### 1. **Clone or extract the repository**

```bash
git clone <repo-url>
cd Machine-Learning-NLP-Pipeline
```
or unpack the ZIP and open in VS Code.


### 2. Set up your Python environment

```bash
python -m venv .venv
# Activate (Windows):
.venv\Scripts\activate
# Activate (Mac/Linux):
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```


📊 Results and Evaluation Outputs
Best Macro-F1: See reports/results_table2.csv

All experiment results: In reports/cv_*.txt

Key evaluation figures: In reports/figures/ (confusion matrix, ROC curve, class dist, etc.)

Test predictions: In reports/best_model_predictions.csv


🧪 Reproducibility
All scripts, config files, and data splits are versioned.

Setting PYTHONPATH and following the run sequence below ensures all imports and scripts work on any system.



📚 References
Chapman et al. (2000). CRISP-DM 1.0

Pennington et al. (2014). GloVe

Reimers & Gurevych (2021). SBERT

[See report for full reference list]


## CETM47 Project: Sequential Code Run Outline

User should follow these steps in order to reproduce all results, figures, and tables for this project.

## 0. Activate your virtual environment

```powershell
.venv\Scripts\activate

```

## 1. Run all unit tests

```powershell
$env:PYTHONPATH = "."
pytest -q
```
- Purpose: To check that core helpers and cleaning functions works




