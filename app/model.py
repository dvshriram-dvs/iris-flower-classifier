import joblib

# Load the trained model once when the application starts
model = joblib.load("model/iris_model.pkl")

# Class names corresponding to model predictions
class_names = [
    "Setosa",
    "Versicolor",
    "Virginica"
]