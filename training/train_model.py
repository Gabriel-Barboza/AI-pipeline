import pandas as pd
import joblib
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

def train_model():
    X_train = pd.read_csv("../data/X_train.csv")
    y_train = pd.read_csv("../data/y_train.csv")
    X_test = pd.read_csv("../data/X_test.csv")
    y_test = pd.read_csv("../data/y_test.csv")

    with mlflow.start_run():
        model = RandomForestClassifier(random_state=42)
        model.fit (X_train, y_train.values.ravel())
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)
        joblib.dump(model, "model.pkl")

        feature_count = X_train.shape[1] 
        initial_type = [('float_input', FloatTensorType([None, feature_count]))]
        onnx_model = convert_sklearn(model, initial_types=initial_type)

        with open("model.onnx", "wb") as f:
            f.write(onnx_model.SerializeToString())
    
        mlflow.log_artifact("model.onnx")
        print(f"Model Accuracy: {accuracy}")


if __name__ == "__main__":
    train_model()