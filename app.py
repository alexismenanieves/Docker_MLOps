# Import libraries
import pickle
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from pydantic import BaseModel
from magnum import Magnum
from typing import List

# Load the model
model_components = pickle.load(open("model_components.pkl", "rb"))
model = model_components["model"]
extras = model_components["extras"]

# Input data validation
class Input(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class ModelInputs(BaseModel):
    inputs: List[Input]
    def return_dict_inputs(cls):
        return [dict(input) for input in cls.all]

ml_models = {}

def species_predictor(x: dict) -> dict:
    with open("model_components.pkl","rb") as model_file:
        model_components = pickle.load(model_file)
        model = model_components["model"]
        prediction = model.predict(x)
        

@asynccontextmanager
async def ml_lifespan_manager(app: FastAPI):
    ml_models['']

