# 🌧️ Next-Day Rain Prediction

This project develops a machine learning model to predict next-day rainfall based on historical weather data. It covers exploratory data analysis (EDA), feature preprocessing, and training a binary classification model. A lightweight web interface is included for demonstrating predictions.

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA) on weather dataset
- 🤖 Machine learning model for binary classification (Rain / No Rain)
- 🌐 Flask-based backend API
- 💻 Simple frontend for user input and prediction
- 🐳 Dockerized for easy setup and deployment

## 🧠 Problem Statement

Predict whether it will rain tomorrow based on current and historical weather conditions.

This is formulated as a **binary classification problem**:

- `1` → Rain
- `0` → No Rain

## 📂 Dataset

- **Source:** Australian Weather Dataset (Kaggle)
- Contains historical weather observations such as:
  - Temperature
  - Humidity
  - Wind speed
  - Pressure
  - Rainfall

> ⚠️ Dataset is not included in this repository. Please download it manually.

## 🏗️ Project Structure

```
.
src/                    # Flask app (inference)
   ├── app.py
   ├── templates/
        └── index.html
   ├── train.ipynb             # EDA / experimentation
   ├── train.py                # training scripts
   ├── data/                   # dataset (optional or ignored)
        └── weatherAUS.csv
   ├── requirements.txt
   ├── Dockerfile
   ├── .dockerignore
   └── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

Open your browser at: http://localhost:5000

## 🐳 Run with Docker

### Build the image

```
docker build -t rain-prediction .
```

### Run the container

```
docker run -p 5000:5000 rain-prediction
```

## 🧪 Model

- Algorithm: Logistic Regression / Random Forest (update as needed)
- Input features: Temperature, Humidity, Wind speed, etc.
- Output: Rain (1) or No Rain (0)

## 📊 Exploratory Data Analysis (EDA)

- Missing value handling
- Feature distribution analysis
- Correlation analysis
- Data preprocessing

## 🛠️ Tech Stack

- Flask
- Scikit-learn
- NumPy
- Docker

## ⚠️ Limitations

- Model trained on Australian dataset → may not generalize globally
- Simplified feature set
- Not optimized for real-time forecasting

## 🚀 Future Improvements

- Improve model accuracy
- Add real-time weather API
- Enhance frontend UI
- Deploy to cloud

## 👤 Author

Abdullah Al Muntakim
Yosakorn Sirisoot
