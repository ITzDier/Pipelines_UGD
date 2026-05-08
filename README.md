# 🎮 Ultimate Games Rating Predictor

---

# 🇺🇸 English Version

## 📌 Project Overview

This project implements an end-to-end **Machine Learning pipeline** designed to predict videogame `user_rating` scores using the *Ultimate Games Dataset* (15,000+ records).

The repository focuses on:

- Data preprocessing
- Feature engineering
- Hyperparameter optimization
- Model training and evaluation
- Standalone inference testing

The final model achieves high predictive accuracy using optimized **Random Forest Regression** techniques.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.11+ |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |
| Algorithm | Random Forest Regressor |
| Optimization | GridSearchCV + Cross Validation |

---

## 🏗️ Project Structure

```text
Pipelines_UGD/
├── data/                # Raw dataset files (.csv)
├── docs/                # Documentation and screenshots
│   └── screenshots/
├── models/              # Serialized trained models (.pkl)
├── notebook/            # EDA and experimentation notebooks
└── scripts/             # Production scripts (cleaning, inference, testing)
```

---

## 📊 Model Performance

After preprocessing 43 original dataset columns and optimizing hyperparameters, the final model achieved:

| Metric | Result |
|---|---|
| R² Score | 0.9600 |
| MAE | 0.0613 |

### Interpretation

- **R² = 0.96** → The model explains 96% of the variance in user ratings.
- **MAE = 0.06** → Average prediction error is only ~0.06 rating points.

---

## ⚙️ Best Hyperparameters

```python
n_estimators = 200
max_depth = 20
min_samples_split = 2
```

---

## 🚀 Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## ▶️ Run Inference Test

To validate the trained model outside Jupyter Notebook:

```bash
python scripts/test_model.py
```

---

## 🧠 Technical Highlights

### ✔ Automated Preprocessing Pipeline

The pipeline integrates:

- Missing value imputation
- Feature scaling
- One-Hot Encoding
- Structured preprocessing workflows

### ✔ High Predictive Accuracy

The low MAE demonstrates that engagement-related variables are highly informative predictors for user ratings.

### ✔ Modular Design

Cleaning, training, and inference logic are decoupled, making the project easier to maintain and extend.

### ✔ Production-Oriented Structure

The repository follows a scalable architecture suitable for future API or deployment integration.

---

# 🇺🇸 Current Features

The project already includes several production-oriented components and best practices:

- FastAPI integration for model serving
- Docker containerization support
- Automated preprocessing pipelines
- Hyperparameter optimization using GridSearchCV
- Modular training and inference architecture
- Serialized model deployment with Joblib
- Cross-validation workflows for model evaluation

---

# 🇪🇸 Versión en Español

## 📌 Descripción General

Este proyecto implementa un pipeline de **Machine Learning** de extremo a extremo para predecir el `user_rating` de videojuegos utilizando el *Ultimate Games Dataset* (15,000+ registros).

El repositorio se enfoca en:

- Preprocesamiento de datos
- Ingeniería de características
- Optimización de hiperparámetros
- Entrenamiento y evaluación del modelo
- Pruebas de inferencia independientes

El modelo final alcanza una alta precisión utilizando técnicas optimizadas de **Random Forest Regression**.

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnología |
|---|---|
| Lenguaje | Python 3.11+ |
| Framework ML | Scikit-learn |
| Procesamiento de Datos | Pandas, NumPy |
| Persistencia del Modelo | Joblib |
| Algoritmo | Random Forest Regressor |
| Optimización | GridSearchCV + Validación Cruzada |

---

## 🏗️ Estructura del Proyecto

```text
Pipelines_UGD/
├── data/                # Archivos del dataset (.csv)
├── docs/                # Documentación y capturas
│   └── screenshots/
├── models/              # Modelos entrenados serializados (.pkl)
├── notebook/            # EDA y experimentación
└── scripts/             # Scripts de producción (limpieza, inferencia, pruebas)
```

---

## 📊 Rendimiento del Modelo

Después de preprocesar 43 columnas originales y optimizar hiperparámetros, el modelo final obtuvo:

| Métrica | Resultado |
|---|---|
| R² Score | 0.9600 |
| MAE | 0.0613 |

### Interpretación

- **R² = 0.96** → El modelo explica el 96% de la varianza de los ratings.
- **MAE = 0.06** → El error promedio es de apenas ~0.06 puntos.

---

## ⚙️ Mejores Hiperparámetros

```python
n_estimators = 200
max_depth = 20
min_samples_split = 2
```

---

## 🚀 Instalación y Configuración

### 1. Crear Entorno Virtual

```bash
python -m venv venv
```

### Activar Entorno

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## ▶️ Ejecutar Prueba de Inferencia

Para validar el modelo entrenado fuera de Jupyter Notebook:

```bash
python scripts/test_model.py
```

---

## 🧠 Aspectos Técnicos Destacados

### ✔ Pipeline Automatizado de Preprocesamiento

El pipeline integra:

- Imputación de valores faltantes
- Escalado de variables
- One-Hot Encoding
- Flujos estructurados de preprocesamiento

### ✔ Alta Precisión Predictiva

El bajo MAE demuestra que las variables de engagement son predictores altamente confiables.

### ✔ Diseño Modular

La lógica de limpieza, entrenamiento e inferencia está desacoplada, facilitando mantenimiento y escalabilidad.

### ✔ Arquitectura Orientada a Producción

La estructura del repositorio está diseñada para futuras integraciones con APIs o despliegues.

---

# 🇪🇸 Características Actuales

El proyecto ya incluye múltiples componentes orientados a producción y buenas prácticas de ingeniería:

- Integración con FastAPI para despliegue del modelo
- Soporte para dockerización
- Pipelines automatizados de preprocesamiento
- Optimización de hiperparámetros con GridSearchCV
- Arquitectura modular para entrenamiento e inferencia
- Despliegue de modelos serializados con Joblib
- Flujos de validación cruzada para evaluación del modelo

---

## ⚖️ License / Licencia

This project is licensed under the MIT License.  
Este proyecto está bajo la Licencia MIT.

---

# 👨‍💻 Author / Autor

**Jesús Blanco Andrade**  
Software Architect in Training
