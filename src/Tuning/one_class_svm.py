from sklearn.svm import OneClassSVM
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer
import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'tuning'))
def get_model():
    return OneClassSVM()

def get_param_grid():
    return {
        'nu': [0.01, 0.05, 0.1],
        'gamma': [0.01, 0.1, 1,'auto'],
        'kernel': ['rbf', 'linear']
    }

def get_scorer():
    def f1_scorer(y_true, y_pred):
        y_pred = np.where(y_pred == -1, 1, 0)
        return f1_score(y_true, y_pred, zero_division=0)
    return make_scorer(f1_scorer)

def tune(df):
    X = df[['returns', 'volatility', 'volume']]
    y = df['label']
    model = get_model()
    grid = GridSearchCV(model, get_param_grid(), scoring=get_scorer(), cv=3)
    grid.fit(X, y)
    return grid