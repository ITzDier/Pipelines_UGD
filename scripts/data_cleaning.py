import pandas as pd
import numpy as np

def clean_game_data(df, target='user_rating'):
    """
    Limpia el dataset de videojuegos eliminando columnas de texto,
    URLs e IDs que no aportan valor predictivo.
    """
    # Lista de columnas a eliminar identificadas durante el laboratorio
    cols_to_drop = [
        target, 'serial_no', 'game_id', 'title', 'release_date',
        'all_genres', 'theme', 'art_style', 'view_dimension', 
        'game_mode', 'controls', 'developers', 'publishers', 
        'all_platforms', 'all_tags', 'available_stores', 
        'cover_image_url', 'official_website', 'url_slug', 
        'description_clean', 'rating_tier', 'metacritic_tier'
    ]
    
    # Filtrar solo las que existen en el DF actual
    existing_cols = [c for c in cols_to_drop if c in df.columns]
    
    X = df.drop(columns=existing_cols)
    y = df[target] if target in df.columns else None
    
    # Manejo de nulos e infinitos
    X = X.replace([np.inf, -np.inf], np.nan)
    
    return X, y