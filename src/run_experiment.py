"""
src/run_experiment.py

Optimized experiment runner for pipeline reproducibility.

Usage:
    python src/run_experiment.py --rep_cfg conf/rep_word_tfidf.yaml --clf svm --data data/tweets.feather --trials 10

Required: src/, conf/, data/ must be at the project root.
"""

import sys
import os
from pathlib import Path
import argparse
import yaml
import pandas as pd
from src.preprocess import build_pipeline
from src.models import mnb, svm, lr, rf
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np
import time

# --- Ensure project root is on sys.path for subprocess calls ---
if not (Path.cwd() / "src").exists():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

def get_classifier(name):
    """Return a classifier instance by name."""
    if name == "mnb":
        return mnb()
    elif name == "svm":
        return svm()
    elif name == "lr":
        return lr()
    elif name == "rf":
        return rf()
    else:
        raise ValueError(f"Unknown classifier: {name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rep_cfg", required=True, help="YAML config for preprocessing/vectorizer")
    parser.add_argument("--clf", required=True, choices=["mnb", "svm", "lr", "rf"], help="Classifier name")
    parser.add_argument("--data", default="data/tweets.feather", help="Input data file (.feather or .csv)")
    parser.add_argument("--trials", type=int, default=10, help="Number of repetitions (default 10)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    args = parser.parse_args()

    # --- Load Data ---
    data_path = Path(args.data)
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {args.data}")
    if data_path.suffix == ".csv":
        df = pd.read_csv(data_path)
    elif data_path.suffix == ".feather":
        df = pd.read_feather(data_path)
    else:
        raise ValueError("Data must be .csv or .feather format")
    if not {"text", "label_name"}.issubset(df.columns):
        raise ValueError("Data must contain columns: 'text' and 'label_name'")
    X = df["text"]
    y = df["label_name"]

    # --- Build Pipeline ---
    pipeline = build_pipeline(args.rep_cfg)
    pipeline.steps.append(("clf", get_classifier(args.clf)))

    # --- Cross-validation & Timing ---
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=args.seed)
    t0 = time.time()
    scores = cross_val_score(pipeline, X, y, scoring="f1_macro", cv=skf, n_jobs=-1)
    duration = time.time() - t0

    mean_score = scores.mean()
    std_score = scores.std()
    print(f"[{args.clf.upper()} + {Path(args.rep_cfg).stem}] Macro-F1 (5-fold): {mean_score:.4f} ± {std_score:.4f}")
    print(f"Cross-val run time: {duration:.1f} seconds")

    # --- Save results ---
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    result_file = reports_dir / f"cv_{args.clf}_{Path(args.rep_cfg).stem}.txt"
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(f"Classifier: {args.clf}\n")
        f.write(f"Config: {args.rep_cfg}\n")
        f.write(f"F1 Macro: {mean_score:.4f} ± {std_score:.4f}\n")
        f.write(f"Fold scores: {np.array2string(scores, precision=4)}\n")
        f.write(f"Train time (s): {duration:.1f}\n")
    print(f"Results written to {result_file}")

if __name__ == "__main__":
    main()
