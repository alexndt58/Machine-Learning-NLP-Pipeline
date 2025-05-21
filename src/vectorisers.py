from sklearn.feature_extraction.text import TfidfVectorizer
def char_tfidf(ngram_lo=5, ngram_hi=8):
    return TfidfVectorizer(analyzer="char", ngram_range=(ngram_lo, ngram_hi), lowercase=False)
def word_tfidf():
    return TfidfVectorizer(analyzer="word", ngram_range=(1,3), min_df=2, max_df=0.9)
