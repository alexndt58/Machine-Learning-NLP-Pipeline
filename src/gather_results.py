import pandas as pd
import re
from pathlib import Path

# Path to your reports directory and pattern for result files
REPORTS_DIR = Path("reports")
pattern = re.compile(r"cv_(\w+)_(\w+)\.txt")  # matches cv_clf_rep.txt

rows = []

# Scan all result files
for f in REPORTS_DIR.glob("cv_*.txt"):
    m = pattern.match(f.name)
    if not m:
        continue
    clf, rep = m.groups()
    with open(f, encoding="utf-8") as fh:
        content = fh.read()
    # Parse Macro-F1 and SD from content
    match = re.search(r"F1 Macro: ([\d.]+) ± ([\d.]+)", content)
    if match:
        macro_f1, std = map(float, match.groups())
    else:
        macro_f1, std = None, None
    rows.append({"Pipeline": f"{rep}+{clf}", "Macro-F1": macro_f1, "±SD": std, "Report File": f.name})

# Create DataFrame
results_df = pd.DataFrame(rows)
results_df = results_df.sort_values("Macro-F1", ascending=False)

# Save to CSV
results_df.to_csv("results_table2.csv", index=False)
print("Aggregated results written to results_table2.csv")
print(results_df)
