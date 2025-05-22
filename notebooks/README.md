# Notebooks Directory

This folder contains all Jupyter notebooks for the project **Real-Time Twitter Topic Classification (CETM47 AS2)**.

## Contents

- `01_eda.ipynb`  
  *Exploratory Data Analysis:*  
  Loads, audits, and visualizes the raw tweet data. Documents data quality, class balance, feature engineering, and outputs EDA plots to `../reports/figures/`.

- `04_eval.ipynb`  
  *Evaluation & Visualization:*  
  Aggregates results from model experiments, generates confusion matrix, ROC curves, and creates summary tables for inclusion in the final report.

## Usage

To execute any notebook:

1. Activate your Python virtual environment:
    ```bash
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

2. Launch Jupyter:
    ```bash
    jupyter notebook
    ```
   or use VS Code’s notebook interface.

3. Open and run the desired notebook cell-by-cell.

## Notes

- All output figures are automatically saved in `../reports/figures/`.
- Please ensure all required data files (see `../data/raw/` and `../data/splits/`) are present before running.
- For best reproducibility, use Python 3.11+ and install dependencies from `../requirements.txt`.

---

**For detailed methodology and code, see the main [README.md](../README.md) and section docs in `../docs/`.**
