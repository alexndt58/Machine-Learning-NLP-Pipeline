# 3. Data Understanding & Preparation

## 3.1 Data Sources

- **Primary:** `CETM47_24_5-AS2-Data.json` (6,443 English tweets; Sep 2019 – Aug 2021)
- **Location:** `data/raw/CETM47_24_5-AS2-Data.json`

## 3.2 Data Quality Audit

| Check                  | Result                  |
|------------------------|------------------------|
| Nulls per column       | 0                      |
| Duplicate texts        | 1 (removed)            |
| Short tweets (<3 tokens)| 46 (removed)           |
| Class imbalance        | pop-culture: 39%, arts & culture: 2% |
| Emoji content          | 0%                     |
| Temporal drift         | COVID spike (Mar 2020) |

- **EDA script:** See `notebooks/01_eda.ipynb` for code and plots.

## 3.3 Exploratory Data Analysis

- **Class distribution:** Severe imbalance (visualized in `class_bar.png`)
- **Token and character counts:** Median 25 tokens, 95th percentile 50 tokens (see `length_hist.png`)
- **Timeline:** Volume spike during pandemic (see `timeline.png`)
- **Hashtag analysis:** Top hashtags differ per topic (see notebook output)

## 3.4 Cleaning & Preprocessing Choices

- **Duplicate and short tweet removal**
- **Regex masking:** URLs (`{{URL}}`), mentions (`{{USER}}`)
- **Case normalization:** All lower-case
- **Stop-word strategies:** Snowball and Twitter-custom (see YAML configs)
- **Tokenization:** Regex for char-gram, spaCy otherwise
- **YAML-driven pipeline:** All configs in `conf/` (e.g., `base.yaml`, `chargram.yaml`)

## 3.5 Data Splitting

- **Stratified 60/20/20 split:** train/val/test in `data/splits/`
- **Temporal holdout:** All tweets from July–August 2021 in `temporal.idx`
- **Feather cache:** Cleaned DataFrame saved as `data/tweets.feather` for reproducibility

## 3.6 Justification & Literature

- **Imbalance management:** Following best practices from Dai et al. (2022) TweetEval.
- **Regex cleaning:** Recommended for noisy user-generated content (Luo et al., 2019).
- **Seeded splits:** Ensures replicability; supports robust model comparison.

## 3.7 Outputs

- `notebooks/01_eda.ipynb` — full EDA, code, and charts
- `data/splits/train.idx`, `val.idx`, `test.idx`, `temporal.idx`
- `reports/figures/class_bar.png`, `length_hist.png`, `timeline.png`

---

**References:**
- Dai, Z. et al. (2022). *TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification*. LREC.
- Luo, Z. et al. (2019). *A review of cleaning methods for Twitter data*. 

