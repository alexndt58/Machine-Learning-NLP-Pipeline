import re, html, yaml
from pathlib import Path
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, cfg): self.cfg = cfg
    def transform(self, X, y=None):
        cleaned = []
        for t in X:
            if self.cfg.get("regex_clean", "basic") == "basic":
                t = re.sub(r"https?://\S+|www\.\S+", "{{URL}}", t)
                t = re.sub(r"@[A-Za-z0-9_]+", "{{USER}}", t)
                t = html.unescape(t)
            if self.cfg.get("lower", True): t = t.lower()
            cleaned.append(t)
        return cleaned
    def fit(self, X, y=None): return self

def build_pipeline(cfg_path):
    cfg = yaml.safe_load(Path(cfg_path).read_text())
    cleaner = TextCleaner(cfg)
    if cfg.get("vectoriser") == "char_tfidf":
        nlo, nhi = map(int, cfg.get("ngrams", "5-8").split('-'))
        vect = TfidfVectorizer(analyzer="char", ngram_range=(nlo, nhi), lowercase=False)
    else:
        vect = TfidfVectorizer(analyzer="word", ngram_range=(1,3))
    return Pipeline([("clean", cleaner), ("vect", vect)])
