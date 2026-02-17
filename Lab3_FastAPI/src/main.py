from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from predict import predict_data

app = FastAPI()

class DiabetesData(BaseModel):
    #Pydantic model for diabetes dataset features, which are a total of 10 features. 
    age: float 
    sex:float 
    bmi: float 
    bp: float 
    s1: float 
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

class PredictResponse(BaseModel):
    # Response model containing predicted diabetes progression value.
    prediction: float

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictResponse)
async def predict_diabetes(diabetes_features: DiabetesData):
    # Predict diabetes progression based on provided features.
    try:
        features = [[
            diabetes_features.age,
            diabetes_features.sex,
            diabetes_features.bmi,
            diabetes_features.bp,
            diabetes_features.s1,
            diabetes_features.s2,
            diabetes_features.s3,
            diabetes_features.s4,
            diabetes_features.s5,
            diabetes_features.s6
        ]]
        
        prediction = predict_data(features)
        return PredictResponse(prediction=float(prediction[0]))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))