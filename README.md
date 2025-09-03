# 🛒 Time Series Forecasting - Product Sales  

![Owner avatar]<img width="1536" height="1024" alt="ChatGPT Image Sep 3, 2025, 04_18_52 PM" src="https://github.com/user-attachments/assets/c491f66c-19c2-47ee-b13c-26ca6bc2adfc" />
  
**Repository:** TGajanan/Time_Series_Forecasting  

---

## 📌 Project Overview  
This project focuses on **forecasting daily product sales** using machine learning and time series analysis.  
The workflow covers:  
- **EDA & Insights**: Analyzing sales trends across stores, locations, holidays, and discounts.  
- **Hypothesis Testing**: Statistical tests confirming the impact of holidays, discounts, and store types on sales.  
- **Modeling**: Built and evaluated models like Linear Regression, Random Forest, and XGBoost.  
- **Deployment**: Flask API with a simple HTML frontend to interactively predict sales.  

---

## 📊 Key Insights  
- Sales are **significantly higher during holidays**.  
- **Discounts boost sales**, but margins should be managed.  
- **Urban stores consistently outperform** rural and suburban stores.  
- Seasonal trends show **time-based patterns** in sales.  

---

## 🚀 Features  
- Machine learning models for sales prediction.  
- Flask API (`/predict`) for real-time forecasting.  
- Frontend form (`index.html`) to enter store details and get predicted sales.  

---

## 🗂️ Repository Structure  
Time_Series_Forecasting/
│── model/ # Saved ML model (joblib)
│── templates/ # HTML frontend
│ └── index.html
│── Product_sales_forecasting_Project.ipynb # Notebook (EDA + modeling)
│── app.py # Flask API for deployment
│── requirements.txt # Dependencies


Focus expansion in urban store locations.

Incorporate advanced time-series models (Prophet, LSTMs) for better accuracy.
