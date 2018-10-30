from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CosineClassifier(BaseEstimator, ClassifierMixin):  
    def __init__(self, X=None):
        self.X = X


    def fit(self, X,y):
        
        self.X = X
        self.y = y
        return self

    def _meaning(self, x):
        # returns True/False according to fitted classifier
        # notice underscore on the beginning
        return True

    def predict(self, X):
        y = np.array(self.y)
        y_ = np.bincount(y)
        ii = np.nonzero(y_)[0]
        values = list(zip(ii,y[ii]))
        final_results = []
        results = [[] for i in values]
        if str(type(self.X)) == "<class 'scipy.sparse.csr.csr_matrix'>":
            for k in range(X.shape[0]):
                for i in range(self.X.shape[0]):
                    for j in range(len(values)):
                        if y[i] == values[j][0]:
                            results[j].append(cosine_similarity([self.X[i].toarray()[0]],[X[k].toarray()[0]])[0][0])
                
                res = [np.mean(c) for c in results]
                final_results.append(res.index(max(res)))
                results = [[] for i in values]
        else:
            X = np.array(X)
            self.X = np.array(self.X)
            for k in range(X.shape[0]):
                for i in range(self.X.shape[0]):
                    for j in range(len(values)):
                        if y[i] == values[j][0]:
                            results[j].append(cosine_similarity([self.X[i]],[X[k]])[0][0])
                
                res = [np.mean(c) for c in results]
                final_results.append(res.index(max(res)))
                results = [[] for i in values]

        return np.array(final_results)

    def score(self, X, y=None):
        # counts number of values bigger than mean
        return (sum(self.predict(X))) 