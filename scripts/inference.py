import joblib
import pandas as pd
import os

def run_prediction(input_data):
    """
    Carga el modelo entrenado y predice el user_rating.
    """
    model_path = os.path.join(os.path.dirname(__file__), '../models/pipeline_final.pkl')
    
    try:
        # Carga el pipeline completo (incluye el preprocesamiento)
        model = joblib.load(model_path)
        
        # Realizar la predicción
        prediction = model.predict(input_data)
        return prediction[0]
        
    except FileNotFoundError:
        return "Error: No se encontró el archivo .pkl en la carpeta models."

if __name__ == "__main__":
    # Ejemplo rápido de uso manual
    print("Sistema de Inferencia de Ratings de Videojuegos cargado.")