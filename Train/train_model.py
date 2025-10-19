import pandas as pd
import joblib
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv")
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv")

    with mlflow.start_run():
        model = RandomForestClassifier(random_state=42)
        model.fit (X_train, y_train.values.ravel())
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)
        joblib.dump(model, "model.pkl")

        print(f"Model Accuracy: {accuracy}")
if __name__ == "__main__":
    train_model()