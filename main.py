from fastapi.dependencies import models
from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI()

model = joblib.load("linearmodel.pkl")

class datascience(BaseModel):
    studyHours: float


# api end point

@app.get("/")
def test():
    return {"message": "uvicorn is running"}

@app.post("/predict")
def datainsert(ds:datascience):
    marks = model.predict([[ds.studyHours]])
    return{"predictionmarks":round(float(marks[0]),2)}
    
      