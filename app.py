from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="AI Pipeline")

model = joblib.load("Train/model.pkl")

@app.post("/")
def home():
    return {"message": "Welcome to the AI Pipeline API"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}