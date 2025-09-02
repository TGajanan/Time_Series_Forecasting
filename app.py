from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/xgb_sales_model.joblib")

@app.route('/')
def home():
    return render_template('index.html')

def preprocess_input(data_json):
    df = pd.DataFrame([data_json])
    
    # Map Discount
    df['Discount'] = df['Discount'].map({1:1, 0:0})
    
    # Compute dayofweek and is_weekend
    df['date'] = pd.to_datetime(df[['year','month','day']])
    df['dayofweek'] = df['date'].dt.dayofweek
    df['is_weekend'] = df['dayofweek'].apply(lambda x: 1 if x>=5 else 0)
    
    # Add lag and rolling features as 0 (for demo purposes)
    for lag in [1,7,14,28]:
        df[f'Sales_lag_{lag}'] = 0
    for roll in [7,14]:
        df[f'Sales_roll_{roll}'] = 0
    
    # Reorder columns exactly as model expects
    columns = [
        'Store_id','Store_Type','Location_Type','Region_Code','Holiday','Discount','#Orders',
        'year','month','day','dayofweek','is_weekend',
        'Sales_lag_1','Sales_lag_7','Sales_lag_14','Sales_lag_28','Sales_roll_7','Sales_roll_14'
    ]
    
    return df[columns].values

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = preprocess_input(data['features_dict'])
        prediction = model.predict(features)[0]
        return jsonify({"predicted_sales": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
