from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

def get_CV_scores(model,X,y,scor='accuracy'):
	kf = KFold(n_splits=5,random_state=42,shuffle=True)
	return cross_val_score(model,X,y,cv=kf,scoring=scor)