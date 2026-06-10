# main.py
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Start the FastAPI web system
app = FastAPI()

# 2. Load our smart brain file
brain = joblib.load("smart_brain.pkl")

# Map the numbers (0, 1, 2) back to real flower names
flower_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}


# 3. Define the rules for incoming data (Pydantic Gatekeeper)
class FlowerMeasurements(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# 4. Create the endpoint where users can send data
@app.post("/predict-flower")
def predict(data: FlowerMeasurements):
    # Convert the incoming data into a simple list of numbers for the brain
    input_data = [
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]
    ]

    # Let the brain make a prediction
    prediction_number = brain.predict(input_data)[0]

    # Convert the prediction number to a real name
    result = flower_names[prediction_number]

    return {"predicted_flower": result}