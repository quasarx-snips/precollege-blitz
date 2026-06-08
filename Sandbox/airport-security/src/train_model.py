import pandas as pd
import joblib 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # Ye line import karo

def train_airport_model():
    # 1. Load data
    file_path = '../data/airport_security_data.csv'
    df = pd.read_csv(file_path)
    
    # 2. Split features and target
    X = df[['weight', 'metal_content', 'organic_content']]
    y = df['is_threat']
    
    # 3. 80-20 Split 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train) 
    

    accuracy = model.score(X_test, y_test)
    print(f"Model trained! Accuracy on test set: {accuracy*100}%")
    
  
    model_save_path = '../models/security_model.pkl'
    joblib.dump(model, model_save_path)
    print("Model saved successfully!")

if __name__ == "__main__":
    train_airport_model()
