import joblib

model = joblib.load("../model/model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")

text = ["I don't love this"]
X = vectorizer.transform(text)

prediction = "Positive" if model.predict(X)[0] == 1 else "Negative"

print("Prediction:", prediction)
