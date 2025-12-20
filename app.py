from fastapi import FastAPI, HTTPException
from schema import output, ip_features
import pandas as pd
import joblib
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FEATURE_COLUMNS = [
    "Weight_kg",
    "Distance_km",
    "Provider_Blue_Dart",
    "Provider_DTDC",
    "Provider_Delhivery",
    "Provider_India_Post",
    "Provider_Private_Avg"
]

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("courier_model_pipeline.pkl")

@app.get("/")
def home():
    return {"message": "Model successfully uploaded!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/predict", response_model=output)
def predict_rate(features: ip_features):
    try:
        input_df = pd.DataFrame([features.dict()])
        input_df = input_df[FEATURE_COLUMNS]

        prediction = model.predict(input_df)[0]
        logging.info(f"Prediction: {prediction}")

        return {"Rate_per_kg_Rs": float(prediction)}

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Prediction failed")
