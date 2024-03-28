from fastapi import FastAPI
from pydantic import BaseModel
import joblib
app=FastAPI()

class soilpred(BaseModel):
      N_SOIL:float
      P_SOIL:float
      K_SOIL:float
      TEMPERATURE:float
      HUMIDITY: float
      ph:float
      RAINFALL:float
      STATE: str
    

soil_model=joblib.load("soil_prediction")
@app.get("/")
def soil():
    return "welcome"

@app.post("/soilpred")
def soildata(soil:soilpred):
     soil_data=[soil.N_SOIL, soil.P_SOIL,soil.K_SOIL, soil.TEMPERATURE, soil.HUMIDITY, 
                soil.ph, soil.RAINFALL, soil.STATE]
     prediction=soil_model.predict([soil_data])

     return {"prediction":prediction}
