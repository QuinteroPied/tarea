from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd

app = FastAPI()

# Cargar el modelo desde MLflow
logged_model = 'runs:/e8a54bcfa86d4d828de332d7f313df0f/modelo_regresion'
model = mlflow.sklearn.load_model(logged_model)

class Data(BaseModel):
    Open: float
    High: float
    Low: float
    Adj_Close: float
    Volume: int

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de predicción"}

@app.post("/predict/")
def predict(data: Data):
    # Convertir los datos de entrada en un DataFrame
    df = pd.DataFrame([data.dict()])
    # Realizar la predicción usando el modelo cargado
    prediction = model.predict(df)
    return {"prediction": prediction[0]}

