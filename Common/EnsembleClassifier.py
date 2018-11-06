from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class EnsembleClassifier (BaseEstimator, ClassifierMixin):  
    def __init__(self):
        self.X = X
        self.classifiers = []

    def fit(self, X,y,classifiers):
        
        for c in classifiers:
            c.fit(X,y)
            self.classifiers.append(c)
        return self

    def _meaning(self, x):
        # returns True/False according to fitted classifier
        # notice underscore on the beginning
        return True

    def predict(self, X):
        final_res = []
        for row in x:
            preds = []
            for c in self.classifiers:
                preds.append(c.predict_proba(X))
            mean = np.mean(preds,axis=1)
            final_res.append(mean.index(max(mean)))

        return np.array(final_res)

    def score(self, X, y=None):
        # counts number of values bigger than mean
        return (sum(self.predict(X))) 