# Breast Cancer Prediction System (XAI + Risk Scoring)

A Machine Learning-based web application that predicts whether a tumor is **Malignant or Benign** and provides a **risk score (0–100)** using a trained model.

## Live Demo

- **Frontend (Vercel):**  
  https://your-frontend.vercel.app  

- **Backend API (Render):**  
  https://your-backend.onrender.com  

## Features

- Predicts Breast Cancer (Malignant / Benign)
- Provides Risk Score (0–100)
- Fast API using Flask
- Deployed using Render & Vercel
- ML Model trained using Scikit-learn & XGBoost
- Clean frontend using HTML, CSS, JavaScript

## Project Structure

## Tech Stack

- Frontend:HTML, CSS, JavaScript (Vercel)
- Backend:Flask (Render)
- Machine Learning:Scikit-learn, XGBoost
- Deployment:Render (Backend), Vercel (Frontend)

## How It Works

1. User enters feature values (tumor characteristics)
2. Frontend sends data to Flask API
3. Model predicts probability
4. Output:
   - Prediction (Malignant / Benign)
   - Risk Score (0–100)

## API Endpoint

### POST `/predict`

#### Request:
```json
{
  "radius_mean": 14.2,
  "texture_mean": 20.1
}