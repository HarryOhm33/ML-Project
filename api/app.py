from fastapi import FastAPI, UploadFile, File
import tempfile
from pydantic import BaseModel
import joblib
import os

from resume_parser.extractor import extract_text
from resume_parser.parser import parse_resume

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


# ------------------------------------
# Parse resume from uploaded file
# ------------------------------------
@app.post("/parse-resume-file")
async def parse_resume_file(file: UploadFile = File(...)):

    # create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        content = await file.read()
        tmp.write(content)
        temp_path = tmp.name

    try:
        # extract text
        text = extract_text(temp_path)

        # parse
        data = parse_resume(text)

        return data

    finally:
        # cleanup
        os.remove(temp_path)
