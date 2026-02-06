import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset
data = pd.read_csv("../data/dataset.csv")

texts = data["text"]
labels = data["label"]

texts = texts.replace("don't", "do_not")


# Convert text to numbers
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Create model folder if not exists
os.makedirs("../model", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "../model/model.pkl")
joblib.dump(vectorizer, "../model/vectorizer.pkl")

print("✅ Model trained and saved successfully")
