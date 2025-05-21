# Step 2: Data Understanding & Preparation

## Data Sources
- Main: CETM47_24_5-AS2-Data.json (6,443 English tweets, 2019–2021)

## Quality Audit
- Duplicates by 'id': 0
- Duplicates by 'text': 1 (removed)
- Nulls: 0
- Class imbalance: pop-culture (39%), arts & culture (2%)
- Short tweets (<3 tokens): 46 (removed)

## EDA Highlights
- Median tokens: 25; 95th percentile: 50
- No emoji content
- Timeline: COVID spike in March 2020; possible drift risk

## Cleaning Choices
- Regex masking of URLs and mentions
- Lowercase conversion
- Snowball and Twitter-specific stopword sets
- YAML-driven pipeline (see `src/preprocess.py`)

## Data Split
- Stratified 60/20/20 for train/val/test
- Temporal holdout: tweets from July-August 2021

*(All details and plots in `notebooks/01_eda.ipynb`; splits in `data/splits/`.)*
