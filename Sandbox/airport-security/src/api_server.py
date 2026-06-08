
import uvicorn
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('../models/security_model.pkl')
# Add this right above your @app.get("/check_security") line:

@app.get("/")
def home():
    return {"message": "Airport Security API is running! Use /check_security to predict."}
@app.get("/check_security")
def predict(weight: int, metal: int, organic: int):
    data = pd.DataFrame([[weight, metal, organic]], 
                        columns=['weight', 'metal_content', 'organic_content'])
    prediction = model.predict(data)
    status = "THREAT DETECTED" if prediction[0] == 1 else "SAFE"
    return {"result": status}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
