from fastapi import FastAPI
import onnxruntime as ort
import numpy as np
from src.api.baseModel import IrisFeatures 
app = FastAPI(title="AI Pipeline Otimizado")

# Carrega a sessão do ONNX
session = ort.InferenceSession("Train/model.onnx")
input_name = session.get_inputs()[0].name
label_name = session.get_outputs()[0].name

@app.get("/")
def home():
    return {"message": "Bem-vindo à API Otimizada!"}

@app.post("/predict")

def predict(features: IrisFeatures):
    
    input_array = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]], dtype=np.float32)

    prediction_result = session.run([label_name], {input_name: input_array})[0]

    return {"prediction": prediction_result[0]}