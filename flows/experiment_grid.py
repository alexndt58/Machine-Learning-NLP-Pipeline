import subprocess, itertools, sys
from pathlib import Path
REPS = ["rep_word_tfidf.yaml", "rep_char_tfidf.yaml", "rep_glove.yaml", "rep_sbert.yaml"]
CLFS = ["mnb","svm","lr","rf"]
def main():
    root = Path(__file__).resolve().parent.parent
    for rep, clf in itertools.product(REPS, CLFS):
        cmd = [
            sys.executable,
            str(root/"src"/"run_experiment.py"),
            "--rep_cfg", str(root/"conf"/rep),
            "--clf", clf,
            "--trials","10",
            "--data", str(root/"tweets.csv")
        ]
        subprocess.run(cmd, check=True)
if __name__ == "__main__":
    main()
