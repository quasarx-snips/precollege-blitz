import joblib
import pandas as pd


model = joblib.load('../models/security_model.pkl')


test_data = pd.DataFrame([
    [10, 80, 0], 
    [10, 10, 0]
], columns=['weight', 'metal_content', 'organic_content'])

predictions = model.predict(test_data)

for i, pred in enumerate(predictions):
    result = "Threat" if pred == 1 else "Safe"
    print(f"Test Sample {i+1}: {result}")
