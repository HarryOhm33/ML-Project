import os
import sys
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Define model path
MODEL_DIR = "ml_model"
MODEL_PATH = os.path.join(MODEL_DIR, "text_model.pkl")

def train_model():
    """Train the model and save it"""
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    texts = [
        "I love programming with JavaScript",
        "Python is great for machine learning",
        "I enjoy developing web applications",
        "Machine learning is amazing",
        "AI will shape the future",
    ]
    
    labels = [0, 1, 0, 1, 1]  # 0 = Web Dev, 1 = ML/AI

    pipeline = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ])

    pipeline.fit(texts, labels)

    joblib.dump(pipeline, MODEL_PATH)
    print(f"✅ Model saved at {MODEL_PATH}")

def predict(text):
    """Load model and make a prediction"""
    if not os.path.exists(MODEL_PATH):
        print("❌ Model not found! Train the model first using: python model.py train", file=sys.stderr)
        sys.exit(1)

    model = joblib.load(MODEL_PATH)
    prediction = model.predict([text])[0]
    return "Web Development" if prediction == 0 else "Machine Learning / AI"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        train_model()

    elif len(sys.argv) > 1:
        # CLI input: python model.py "some text"
        text = " ".join(sys.argv[1:])
        print(predict(text))

    else:
        try:
            # Node.js stdin input: expects JSON
            input_data = sys.stdin.read().strip()
            if not input_data:
                print("❌ No input received. Provide text as JSON or as CLI argument.", file=sys.stderr)
                sys.exit(1)

            data = json.loads(input_data)
            text = data.get("input")

            if not text:
                print("❌ Invalid input format. Expected JSON with an 'input' key.", file=sys.stderr)
                sys.exit(1)

            print(predict(text))

        except json.JSONDecodeError:
            print("❌ Invalid JSON input. Make sure to send a properly formatted JSON object.", file=sys.stderr)
            sys.exit(1)
