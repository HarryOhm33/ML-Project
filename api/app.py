from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# -----------------------------
# app initialization
# -----------------------------
app = FastAPI(title="Text Classification API")

# -----------------------------
# build absolute paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "..", "model", "vectorizer.pkl")

# -----------------------------
# load model once (on startup)
# -----------------------------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# -----------------------------
# request schema
# -----------------------------
class PredictRequest(BaseModel):
    text: str


# -----------------------------
# response schema
# -----------------------------
class PredictResponse(BaseModel):
    prediction: str


# -----------------------------
# health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "API running"}


# -----------------------------
# prediction endpoint
# -----------------------------
@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    X = vectorizer.transform([request.text])
    result = model.predict(X)[0]

    label = "Positive" if result == 1 else "Negative"

    return {"prediction": label}
