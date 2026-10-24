import os
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train():
    mlflow.set_experiment("Wine_Quality_Prediction")
    
    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2, random_state=42)
    
    with mlflow.start_run():
        n_estimators = 100
        max_depth = 5
        
        clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        clf.fit(X_train, y_train)
        
        preds = clf.predict(X_test)
        acc = accuracy_score(y_test, preds)
        
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", acc)
        
        mlflow.sklearn.log_model(clf, "model", registered_model_name="WineClassifierModel")
        
        joblib.dump(clf, "model.joblib")
        print(f"Model trained successfully with accuracy: {acc}")

if __name__ == "__main__":
    train()
