from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def mnb(): return MultinomialNB()
def svm(C=1.0): return LinearSVC(C=C)
def lr(C=1.0, penalty="l2"): return LogisticRegression(max_iter=1000, C=C, penalty=penalty)
def rf(n_estimators=200, max_depth=None): return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, n_jobs=-1)
