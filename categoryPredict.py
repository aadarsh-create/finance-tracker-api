import joblib
from pathlib import Path
from models import returnCategory

MODEL_PATH = Path(__file__).parent / "categorizer_model.pkl"
_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def category_predict(description: str) -> returnCategory :
    model = get_model()
    pred = model.predict([description])[0]
    proba = model.predict_proba([description])[0]
    confidence = float(max(proba))
    return {"description":description,"category": pred, "confidence": round(confidence, 3)}