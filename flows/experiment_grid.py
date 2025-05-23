"""
flows/experiment_grid.py

Orchestrates the experiment grid over representations and classifiers.

Usage:
    python flows/experiment_grid.py
"""

import subprocess
from pathlib import Path
import os

# --- Define the grid ---
REPRESENTATION_CONFIGS = [
    "conf/rep_word_tfidf.yaml",
    "conf/rep_chargram.yaml",
    "conf/rep_glove.yaml",
    # Add more YAML configs as needed
]

CLASSIFIERS = ["mnb", "svm", "lr", "rf"]

DATA_PATH = "data/tweets.feather"   # Change if your data location differs
TRIALS = 10

def main():
    project_root = Path(__file__).resolve().parent.parent

    for rep_cfg in REPRESENTATION_CONFIGS:
        for clf in CLASSIFIERS:
            cmd = [
                str(project_root / "src" / "run_experiment.py"),
                "--rep_cfg", rep_cfg,
                "--clf", clf,
                "--data", DATA_PATH,
                "--trials", str(TRIALS)
            ]
            print(f"\nRunning: {os.path.basename(rep_cfg)} + {clf.upper()} ...")
            result = subprocess.run(
                [str(project_root / ".venv" / "Scripts" / "python.exe")] + cmd,
                check=False,
                env={**os.environ, "PYTHONPATH": str(project_root)}
            )
            if result.returncode != 0:
                print(f"Experiment FAILED for {rep_cfg} + {clf}")
            else:
                print(f"Completed {rep_cfg} + {clf}")

if __name__ == "__main__":
    main()
