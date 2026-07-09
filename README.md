# 🌾 OptiCrop

## Smart Agricultural Production Optimization Engine

OptiCrop is a Machine Learning-based web application developed to help farmers identify the most suitable crop based on soil nutrients and environmental conditions. The system uses a Random Forest Classifier trained on agricultural data to provide accurate crop recommendations through a simple and user-friendly web interface.

---

## 📌 Features

- 🌱 Smart Crop Recommendation
- 📊 Prediction Confidence Score
- 🌾 Crop Information Display
- 💻 Responsive and User-Friendly Interface
- 🤖 Machine Learning-Based Prediction
- ⚡ Fast and Accurate Recommendations

---

## 🛠 Technologies Used

### Programming Language
- Python

### Web Framework
- Flask

### Machine Learning
- Scikit-learn (Random Forest Classifier)

### Data Processing
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3

### Model Storage
- Joblib

---

## 🧠 Machine Learning Algorithm

**Random Forest Classifier**

The model is trained using the Crop Recommendation Dataset and predicts the most suitable crop based on the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The trained model achieves approximately **99% prediction accuracy**.

---

## 📂 Dataset

**Crop Recommendation Dataset**

The dataset contains agricultural information including:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall
- Crop Label

---

## 📁 Project Structure

```text
OptiCrop/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── model/
│   └── crop_model.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── screenshots/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/OptiCrop.git
```

Move into the project folder:

```bash
cd OptiCrop
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

> Add screenshots of:
>
> - Home Page
> - Prediction Result Page

Store them inside the **screenshots** folder.

---

## 🎯 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation
- Irrigation Recommendation
- Disease Detection using Deep Learning
- Interactive Analytics Dashboard

---

## 👩‍💻 Author

**Madupalli Akanksha**

B.Tech - Computer Science and Engineering

---

## 📄 License

This project is developed for educational and internship purposes.