from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

def get_CV_scores(model,X,y,scor='accuracy'):
    kf = KFold(n_splits=5,random_state=42,shuffle=True)
    return cross_val_score(model,X,y,cv=kf,scoring=scor)

def get_classification_report(model,X,y_true, target_names = ['DOC','ENTER','ORG','PRIV','RANG','HOST']):
    X_train, X_test, y_train, y_test = train_test_split(X, y_true, test_size=0.33, random_state=42,shuffle=True)
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred, target_names=target_names)