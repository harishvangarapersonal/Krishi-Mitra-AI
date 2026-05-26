# 🌱 Krishi-Mitra AI

### An Intelligent Farming Assistant for Indian Farmers

Krishi-Mitra AI is an AI-powered smart farming assistant developed to help farmers make data-driven agricultural decisions using Machine Learning, Real-time APIs, and Computer Vision.

This project was developed as part of the **Smart India Hackathon (SIH)** problem statement and successfully got selected at the **college level**.

---

# 🚀 Features

## 🌱 Crop Recommendation

Recommends the best crop based on:

* Soil nutrients (N, P, K)
* pH values
* Temperature
* Rainfall
* Humidity
* State-wise agricultural conditions

---

## 🌾 Yield Prediction

Predicts crop yield using:

* State
* Crop type
* Season
* Area cultivated

---

## 🦠 Disease Detection

Farmers can upload crop leaf images and the CNN model detects:

* Plant disease
* Confidence score

Built using TensorFlow/Keras.

---

## 🤖 AI Chatbot

Integrated with Google Gemini API to provide:

* Farming guidance
* Crop suggestions
* Agricultural support

---

## 🌍 Sustainability Score

Evaluates sustainability based on:

* Water usage
* Crop rotation
* Resource efficiency

---

# 🧠 Our Innovation

Instead of using a single generic model, we built:

✅ State-wise AI models for:

* Andhra Pradesh
* Telangana
* Jharkhand

Because each state has:

* Different soil composition
* Different weather conditions
* Different crop patterns

This improved prediction accuracy and provided localized recommendations.

---

# 🏗️ Project Architecture

Frontend (React / Mobile UI)
⬇
Flask Backend Server
⬇
AI Models + External APIs
⬇
Prediction Results

### External APIs Used:

* SoilGrids API → Soil Data
* OpenWeather API → Weather Data
* Google Gemini API → AI Chatbot

---

# 🛠️ Tech Stack

## Backend

* Python
* Flask
* Scikit-learn
* TensorFlow / Keras
* Pandas
* NumPy

## Frontend

* React
* TypeScript
* Figma

## APIs & Cloud

* Google Colab
* OpenWeather API
* SoilGrids API
* Google Gemini API

## Development Tools

* VS Code
* Postman
* GitHub

---

# 📊 Datasets Used

We used multiple datasets for:

* Crop Recommendation
* Yield Prediction
* Disease Detection

Sources:

* Kaggle
* Government portals
* Agricultural APIs

---

# 🚧 Challenges We Faced

## Dataset Issues

* Missing values
* Duplicate crop names
* Empty columns
* Inconsistent formats

We solved this using:

* Data cleaning
* Data preprocessing
* Feature engineering

---

## Local System Problems

We faced:

* TensorFlow installation issues
* PATH errors
* pip failures

To solve this, we shifted model training to:
✅ Google Colab

---

## Large Disease Dataset

Disease dataset contained:

* 54K+ images
* ~3GB data

We used Colab GPU acceleration for faster training.

---

# ⚡ How It Works

1. Farmer opens the app
2. System fetches:

   * Soil data
   * Weather data
   * Rainfall
3. AI models process inputs
4. App provides:

   * Crop recommendation
   * Yield prediction
   * Disease detection
   * Sustainability score

---

# 🏆 Achievements

✅ Successfully developed a complete AI-powered agriculture assistant
✅ Built multiple state-wise AI models
✅ Integrated real-time APIs
✅ Developed CNN-based disease detection
✅ Selected at College Level for Smart India Hackathon (SIH)

---

# 🔮 Future Enhancements

* Fertilizer Recommendation
* Market Price Prediction
* Voice Assistant
* IoT Sensor Integration
* Drone-based Monitoring

---

# 👨‍💻 Team

Developed with teamwork, problem-solving, and innovation to empower Indian farmers using Artificial Intelligence.

