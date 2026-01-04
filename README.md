# Courier Price Prediction API

A **FastAPI-based machine learning web service** that predicts courier rates per kg based on package weight, distance, and courier provider. The project demonstrates building, containerizing, and deploying a machine learning model using Python, FastAPI, Docker, and Render.

---
Live Deployment

The API is deployed and live on Render:

https://courier-price-prediction-app.onrender.com/




## Project Overview

This project uses a pre-trained machine learning model (`courier_model_pipeline.pkl`) to predict courier rates. The FastAPI application provides a RESTful API to interact with the model. The application is fully containerized using Docker and deployed live on Render.

The app allows users to:

- Check API health status
- Get courier rate predictions by providing input features like weight, distance, and provider selection

---

## Features

- **FastAPI** backend for serving machine learning predictions  
- **CORS-enabled** for cross-origin requests  
- **Model loading at startup** for faster response  
- **Dockerized** for easy deployment  
- **Live deployment** on Render  

---

## File Structure

```
courier-price-prediction/
├── app.py                     # FastAPI application with endpoints
├── schema.py                  # Pydantic models for input/output validation
├── courier_model_pipeline.pkl  # Pre-trained ML model
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration file
└── __pycache__/               # Python cache files (ignored in Docker)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/SiddharthGanguli/courier-price-prediction-app.git
cd courier-price-prediction
pip install -r requirements.txt
docker build -t courier-price-api .
docker run -p 8000:8000 courier-price-api
```
The app will be accessible at http://localhost:8000

## Usage

### Base URL

http://localhost:8000/

---

## API Endpoints

### 1. Home

**Endpoint**
```json
GET /
```
**Response**
```json
{
  "message": "Model successfully uploaded!"
}
```
2. Health Check

Endpoint
```json
GET /health
```
Response
```json
{
  "status": "ok"
}
```
3. Predict Courier Rate

Endpoint
```json
POST /api/v1/predict
```
JSON Body for prediction endpoint will be in this way 
```json
{
  "Weight_kg": 2.5,
  "Distance_km": 10,
  "Provider_Blue_Dart": true,
  "Provider_DTDC": false,
  "Provider_Delhivery": false,
  "Provider_India_Post": false,
  "Provider_Private_Avg": false
}
```
Response
```json

{
  "Rate_per_kg_Rs": 150.0
}
```
