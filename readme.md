# 🚀 ML Model Integration with Node.js

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Node.js](https://img.shields.io/badge/Node.js-18.x-green?style=for-the-badge&logo=node.js)
![Express](https://img.shields.io/badge/Express.js-black?style=for-the-badge&logo=express)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)

This project integrates a **Machine Learning model** with a **Node.js backend** using **Python (Scikit-Learn)**. The backend communicates with a Python script via `child_process.spawn()` to generate predictions.

📌 **GitHub Repo:** [ML-Project](https://github.com/HarryOhm33/ML-Project)

---

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/HarryOhm33/ML-Project.git
cd ML-Project
```

### **2️⃣ Create a Virtual Environment**

```sh
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```sh
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install
```

### **4️⃣ Set Up Environment Variables**

Create a `.env` file in the root directory:

```ini
PORT=7001
PYTHON_SCRIPT_PATH=ml_model/model.py
```

### **5️⃣ Run the Server**

```sh
node server.js
```

---

## ⚡ Running the ML Model via CLI

### **Train the Model**

```sh
python ml_model/model.py train
```

### **Test the Model with Input**

```sh
python ml_model/model.py "I love coding in Python"
```

Expected Output:

```sh
Prediction: Positive
```

---

## 🔥 Project Structure

```
📦 ML-Project
├── 📂 controllers         # Backend controllers
│   ├── mlController.js    # ML model integration
├── 📂 ml_model            # Machine Learning model
│   ├── model.py           # Python script
│   ├── text_model.pkl     # Trained ML model
├── 📂 routes              # Express.js routes
│   ├── mlRoutes.js        # ML API routes
├── 📂 venv                # Virtual environment (ignored in Git)
├── .env                   # Environment variables
├── .gitignore             # Ignored files
├── package.json           # Node.js dependencies
├── requirements.txt       # Python dependencies
├── server.js              # Express server
└── README.md              # Project documentation
```

---

## ⚡ API Endpoints

### **🔹 Run ML Model**

**Endpoint:** `POST /api/ml/predict`  
**Description:** Sends text data to the ML model and returns a prediction.

#### **🔹 Request**

```json
{
  "text": "Your input text here"
}
```

#### **🔹 Response**

```json
{
  "prediction": "ML model output"
}
```

---

## 🖥️ CLI Testing (cURL)

### **Test API with cURL**

After running the server, test the API using `cURL`:

```sh
curl -X POST http://localhost:7001/api/ml/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!"}'
```

Expected Response:

```json
{
  "prediction": "ML model output"
}
```

---

## 📌 Technologies Used

- **Backend:** Node.js, Express.js
- **Machine Learning:** Python, Scikit-Learn
- **Interfacing:** `child_process.spawn()`

---

## 💡 Future Improvements

- ✅ Add **authentication** for API security
- ✅ Deploy the backend to a cloud service
- ✅ Train a more advanced ML model

---

## 📜 License

This project is **MIT Licensed**.

🔹 **Developed by [HarryOhm33](https://github.com/HarryOhm33)** 🚀
