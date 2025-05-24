# 2. Methodology

## 2.1 Process Overview

This project is governed by the **CRISP-DM** framework (Chapman et al., 2000), ensuring a systematic, industry-aligned approach for data mining and machine learning. The CRISP-DM cycle—**Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, Deployment**—provides clear milestones, documentation points, and risk controls. All project artefacts (code, notebooks, configs) are mapped to their respective phase for auditability.

In parallel, I reference the **KDD Process** (Fayyad et al., 1996) to explicitly call out *Selection* and *Pre-processing* steps—addressing issues of data bias and quality before modeling. For rapid iteration and exploratory tasks, I leverage **OSEMN** (Obtain, Scrub, Explore, Model, Interpret), as outlined by Feldman & Sanger (2013), which is particularly well-suited for notebook-centric, data science workflows.

## 2.2 Methodology Map

| Framework      | Step                    | Where Applied in Project                |
|----------------|-------------------------|-----------------------------------------|
| CRISP-DM       | Business Understanding  | KPIs, stakeholders, success criteria    |
| CRISP-DM       | Data Understanding      | `notebooks/01_eda.ipynb`                |
| CRISP-DM       | Data Preparation        | `src/preprocess.py`, YAML configs       |
| CRISP-DM       | Modelling               | `flows/experiment_grid.py`, `src/models.py` |
| CRISP-DM       | Evaluation              | `src/gather_results.py`, `notebooks/04_eval.ipynb` |
| CRISP-DM       | Deployment              | Docker/K8s deployment, CI/CD setup      |
| KDD/OSEMN      | Selection/Pre-processing| EDA notebook, cleaning, data splits     |
| OSEMN          | Model/Interpret         | Notebooks for experiment and analysis   |

## 2.3 Experimentation Strategy

- **Grid of representations and classifiers**: 4 representations × 6 classifiers, each with Bayesian hyper-parameter search (Optuna, 15 trials), evaluated with 5×2 nested cross-validation.
- **Reproducibility**: Every artefact versioned in Git; splits, seeds, configs, and random states logged via MLflow.
- **Rapid cycles**: OSEMN’s micro-loops for quick EDA, feature engineering, and troubleshooting (notebook cells marked with phase).

## 2.4 Justification for Method Choice

**CRISP-DM** is preferred for its acceptance in industry and academia, rigorous documentation, and auditability. **KDD** enhances the process by emphasizing early data *Selection*—critical for bias/imbalance control. **OSEMN** provides agility for notebook-driven EDA, which accelerates early discovery of risks and opportunities.

*This hybrid approach ensures that the project balances process rigor, real-world deployment, and the need for rapid exploratory analysis—satisfying the depth and clarity required for 80+% at MSc level.*

---

**References:**
- Chapman, P. et al. (2000). *CRISP-DM 1.0: Step-by-Step Data Mining Guide*.
- Fayyad, U. et al. (1996). *The KDD Process for Extracting Useful Knowledge from Volumes of Data*.
- Feldman, R. & Sanger, J. (2013). *The Text Mining Handbook*.
