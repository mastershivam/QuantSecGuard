from sklearn.ensemble import IsolationForest
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer
import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'tuning'))
def get_model():
    return IsolationForest(random_state=42)

def get_param_grid():
    return {
        'n_estimators': [100, 200, 300],
        'contamination': [0.005, 0.01, 0.02],
        'max_features': [1.0, 0.75, 0.5],
        'random_state': [1,2,3,4]
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