import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn


# Cargar datos
data = pd.read_csv('Tarea2/AAPL.csv')
print(data.head())

# Definir features y target
X = data[['Open', 'High', 'Low', 'Adj Close', 'Volume']]
y = data['Close']

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Iniciar un experimento en MLflow
mlflow.set_experiment("regresion_lineal_aapl")

# Entrenar el modelo y registrar en MLflow
with mlflow.start_run() as run:
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Predecir
    y_pred_train = modelo.predict(X_train)
    y_pred_test = modelo.predict(X_test)

    # Evaluar
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)

    # Loguear parámetros, métricas y modelo
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("mse_train", mse_train)
    mlflow.log_metric("mse_test", mse_test)
    mlflow.log_metric("r2_train", r2_train)
    mlflow.log_metric("r2_test", r2_test)
    mlflow.sklearn.log_model(modelo, "modelo_regresion")

    run_id = run.info.run_id
    print(f"Run ID: {run_id}")
