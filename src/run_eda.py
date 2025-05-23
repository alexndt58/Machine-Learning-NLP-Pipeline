import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import re
import collections
import emoji

# ========== SETUP ==========
RAW_DATA = Path("data/raw/CETM47_24_5-AS2-Data.json")
FEATHER_OUT = Path("data/tweets.feather")
FIG_DIR = Path("reports/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ========== LOAD ==========
print(f"Loading {RAW_DATA}...")
df = pd.read_json(RAW_DATA)
print(f"Loaded {len(df)} tweets.")

# ========== AUDIT ==========
print("Nulls per column:", df.isnull().sum().to_dict())
print("Duplicate texts:", df['text'].duplicated().sum())

df = df.drop_duplicates(subset='text')
df['token_len'] = df['text'].str.split().apply(len)
short_tweets = df[df['token_len'] < 3]
print(f"Short tweets (<3 tokens): {len(short_tweets)}")
df = df[df['token_len'] >= 3].copy()

# ========== CLASS DISTRIBUTION ==========
plt.figure(figsize=(8,4))
sns.countplot(x='label_name', data=df, order=df['label_name'].value_counts().index)
plt.title("Tweet class distribution")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(FIG_DIR / "class_bar.png")
plt.close()

# ========== LENGTH STATS ==========
df['char_len'] = df['text'].str.len()
fig, axs = plt.subplots(1,2, figsize=(10,4))
sns.histplot(df['token_len'], bins=30, kde=True, ax=axs[0], color='steelblue')
axs[0].set_title("Token count per tweet")
sns.histplot(df['char_len'], bins=30, kde=True, ax=axs[1], color='orange')
axs[1].set_title("Character count per tweet")
plt.tight_layout()
plt.savefig(FIG_DIR / "length_hist.png")
plt.close()

# ========== TIMELINE ==========
df['date'] = pd.to_datetime(df['date'])
timeline = df.set_index('date').resample('D').size()
plt.figure(figsize=(12,3))
timeline.plot()
plt.title("Tweets per day (time series)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(FIG_DIR / "timeline.png")
plt.close()

# ========== HASHTAG ANALYSIS ==========
def extract_hashtags(text):
    return re.findall(r"#\w+", text)

hashtag_counts = {}
for topic in df['label_name'].unique():
    hashtags = sum(df.loc[df['label_name']==topic, 'text'].apply(extract_hashtags), [])
    hashtag_counts[topic] = collections.Counter(hashtags).most_common(5)
print("Top hashtags per class:")
for k, v in hashtag_counts.items():
    print(f"{k}: {v}")

# ========== EMOJI PRESENCE ==========
def has_emoji(s):
    return any(char in emoji.EMOJI_DATA for char in s)
df['has_emoji'] = df['text'].apply(has_emoji)
print(f"Percent of tweets with emoji: {df['has_emoji'].mean()*100:.2f}%")

# ========== SAVE FEATHER ==========
df.reset_index(drop=True).to_feather(FEATHER_OUT)
print(f"Saved cleaned DataFrame to {FEATHER_OUT}")

print("EDA complete: figures in reports/figures/, cleaned data in data/tweets.feather.")


#==========AUTOMATICALLY SAVE AS A TEXT FILE IN EDA SCRIPT ========
with open("reports/eda_summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Loaded {len(df)} tweets.\n")
    f.write(f"Nulls per column: {df.isnull().sum().to_dict()}\n")
    f.write(f"Duplicate texts: {df['text'].duplicated().sum()}\n")
    f.write(f"Short tweets (<3 tokens): {len(df[df['token_len'] < 3])}\n")
    f.write("Top hashtags per class:\n")
    for k, v in hashtag_counts.items():
        f.write(f"{k}: {v}\n")
    f.write(f"Percent of tweets with emoji: {df['has_emoji'].mean()*100:.2f}%\n")

