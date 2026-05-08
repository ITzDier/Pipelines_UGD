import joblib
import pandas as pd
import os

def test_system():
    # 1. Rutas relativas para que funcione desde la carpeta raíz
    model_path = 'models/pipeline_final.pkl'
    
    print("--- INICIANDO PRUEBA RÁPIDA DEL MODELO ---")
    
    if not os.path.exists(model_path):
        print(f"Error: No se encontró el modelo en {model_path}")
        return

    # 2. Cargar el Pipeline (incluye preprocesamiento y el RandomForest)
    model = joblib.load(model_path)
    print("✓ Modelo cargado exitosamente.")

    # 3. Creamos un 'juego ficticio' para probar
    # Usar los mismos nombres de columnas que quedaron en X tras la limpieza
    juego_prueba = pd.DataFrame([{
        'release_year': 2026,
        'popularity_score': 95.5,
        'engagement_score': 88.0,
        'metacritic': 90.0,
        'reviews_count': 1500,
        'is_multiplayer': 1,
        'platform_count': 3,
        'game_series_count': 1,
        'status_playing': 50,
        'library_count': 200,
        'status_dropped': 10,
        'avg_playtime_hours': 40.5,
        'status_toplay': 100,
        'status_owned': 500,
        'ratings_count': 1200,
        'is_multi_platform': 1,
        'status_beaten': 80,
        'status_yet': 30,
        'achievements_count': 50,
        'esrb_rating': 'Teen', # El pipeline se encarga de codificar esto
        'decade': 2020
    }])

    # 4. Predicción
    # El pipeline se encarga de escalar los números automáticamente
    try:
        resultado = model.predict(juego_prueba)
        print(f"\nDATOS DEL JUEGO DE PRUEBA:")
        print(juego_prueba.to_string(index=False))
        print(f"\n>>> RATING DE USUARIO PREDICHO: {resultado[0]:.2f}")
        print("\n--- PRUEBA FINALIZADA CON ÉXITO ---")
    except Exception as e:
        print(f"Error durante la predicción: {e}")

if __name__ == "__main__":
    test_system()