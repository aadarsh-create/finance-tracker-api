import joblib
from pathlib import Path
from models import returnType

MODEL_PATH = Path(__file__).parent / "type_model.pkl"
_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def type_predict(description: str) -> returnType:
    model = get_model()
    pred = model.predict([description])[0]
    proba = model.predict_proba([description])[0]
    confidence = float(max(proba))
    return {"description":description,"type": pred, "confidence": round(confidence, 3)}