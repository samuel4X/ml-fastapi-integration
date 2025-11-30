from pathlib import Path
import joblib
from sklearn.datasets import load_iris
import numpy as np

MODEL_PATH = Path(__file__).parent / "iris_model.pkl"

try:
    _model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise RuntimeError(f"This path {MODEL_PATH} was not found")

iris_data = load_iris()
LABEL_TO_NAME = {i: name for i, name in enumerate(iris_data.target_names)}


def predict_species(features: list) -> tuple[str, float]:

    input_array = np.array([features])
    
    prediction_index = _model.predict(input_array)[0]
    
    species_name = LABEL_TO_NAME.get(int(prediction_index), "unknown")

    prediction_proba = _model.predict_proba(input_array)[0]

    confidence = float(np.max(prediction_proba))
    
    return species_name, confidence