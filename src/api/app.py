from fastapi import FastAPI
import onnxruntime as ort
import numpy as np
from .baseModel import IrisFeatures 
from pathlib import Path



app = FastAPI(title="AI Pipeline ", description="""
Uma API que utiliza um modelo de Machine Learning (ONNX) para 
classificar a espécie de uma flor de Íris (setosa, versicolor, virginica) 
com base nas 4 medidas de suas pétalas e sépalas.
    """
)
session = ort.InferenceSession("models/model.onnx")
input_name = session.get_inputs()[0].name
label_name = session.get_outputs()[0].name

@app.get("/")
def home():
    return {"message": "Bem-vindo à API Íris!"}


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