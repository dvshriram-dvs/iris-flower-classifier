![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🌸 Iris Flower Classifier API & Web UI

A Machine Learning web application built with **FastAPI**, **Scikit-learn**, and **HTML/CSS/JavaScript** that predicts the species of an Iris flower based on its measurements.

## 🚀 Live Demo

**Web App:** https://iris-flower-classifier-1.onrender.com

## ✨ Features

- 🌸 Predicts Iris flower species
- ⚡ FastAPI REST API
- 💻 Interactive Web Interface
- 📊 Confidence Score
- ✅ Input Validation using Pydantic
- 📖 Automatic Swagger API Documentation
- ☁️ Deployed on Render

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- Joblib
- HTML
- CSS
- JavaScript
- Uvicorn
- Render

---

## 📂 Project Structure

```text
iris-flower-classifier/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── templates/
│       └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── model/
│   └── iris_model.pkl
│
├── train_model.py
├── requirements.txt
├── render.yaml
└── README.md
```

---

## 🧠 Machine Learning Model

Dataset:
- Iris Dataset (Scikit-learn)

Algorithm:
- Random Forest Classifier

Features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Output Classes:
- Setosa
- Versicolor
- Virginica

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dvshriram-dvs/iris-flower-classifier.git
cd iris-flower-classifier
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### Home

```
GET /
```

Returns the web interface.

---

### Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

### Predict

```
POST /predict
```

Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response

```json
{
  "prediction": "Setosa",
  "confidence": 100.0
}
```

---

## 📖 API Documentation

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

---

## 🚀 Deployment

The application is deployed on **Render**.

---

## 👨‍💻 Author

**D V Shriram**
Student at VIT Bhopal University

GitHub: https://github.com/dvshriram-dvs

---

## 📄 License

This project is licensed under the MIT License.
