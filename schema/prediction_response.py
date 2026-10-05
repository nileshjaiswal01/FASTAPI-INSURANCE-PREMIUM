from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category :str= Field(..., description="the predicted insurance premium category",example="High")

    confidence: float= Field (..., description="Model confidence for the predicted class (range: 0 to 1)",example=0.8432)

    class_probabilities : Dict[str,float] = Field(..., description="prob distribution accross all class",example={"low":0.01,"medium":0.15,"High":0.84})