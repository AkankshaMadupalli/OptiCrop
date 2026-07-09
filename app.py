from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model/crop_model.pkl")

# Crop Information
crop_info = {
    "rice": {
        "season": "Kharif",
        "temperature": "20–30°C",
        "ph": "5.5–7.0",
        "water": "High",
        "description": "Rice grows best in warm and humid climates with abundant water."
    },
    "maize": {
        "season": "Kharif",
        "temperature": "18–27°C",
        "ph": "5.5–7.5",
        "water": "Medium",
        "description": "Maize prefers fertile soil and moderate rainfall."
    },
    "cotton": {
        "season": "Kharif",
        "temperature": "21–30°C",
        "ph": "5.8–8.0",
        "water": "Medium",
        "description": "Cotton requires warm weather and well-drained black soil."
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get input values
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    # Create DataFrame
    data = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    )

    # Predict crop
    prediction = model.predict(data)[0]

    # Prediction confidence
    probabilities = model.predict_proba(data)
    confidence = round(max(probabilities[0]) * 100, 2)

    # Get crop information
    info = crop_info.get(
        prediction.lower(),
        {
            "season": "Not Available",
            "temperature": "Not Available",
            "ph": "Not Available",
            "water": "Not Available",
            "description": "Information is not available for this crop."
        }
    )

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        info=info
    )


if __name__ == "__main__":
    app.run(debug=True)