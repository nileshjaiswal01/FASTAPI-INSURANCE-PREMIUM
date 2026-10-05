from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from schema.user_input import UserInput
from Model.predict import predict_output,model,MODEL_VERSION
from schema.prediction_response import PredictionResponse

# import the ml model

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Insurance company"}

@app.get("/health")
def health_care():
    return{
        "status":"ok",
        "model_version": MODEL_VERSION,
        "model_lodaded": model is not None
        }

@app.post('/predict')
def predict_premium(data: UserInput):

    User_Input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:

        prediction = model.predict(User_Input)[0]

        return JSONResponse(status_code=200, content={'predicted_category': prediction,"age_group":data.age_group})
    
    except Exception as e:

        return JSONResponse(status_code=500,content=str(e))



