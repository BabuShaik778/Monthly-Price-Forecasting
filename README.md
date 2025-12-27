# Monthly-Price-Forecasting

📈 Monthly Price Forecasting and Decision Support System

Project Overview :

This project develops a predictive model to forecast average monthly prices for the next 12 months using historical data. It provides actionable insights for businesses to optimize inventory, pricing, and marketing strategies based on predicted price trends.

Business Context:

Businesses require accurate price forecasts to make informed procurement and sales decisions. This project leverages time series forecasting to anticipate price changes, enabling strategic planning and risk mitigation.

Dataset :

Source: Provided CSV file with historical monthly prices.

Data Dictionary: Includes date, average monthly price, and additional relevant features.

Preprocessing:

Handled missing values using forward fill (ffill).

Detected and removed outliers using IQR method.

Corrected anomalies via interpolation or median replacement.


Methodology

1. Data Cleaning

Ensures consistent, reliable data for forecasting.

2. Model Selection

Prophet (Facebook): Chosen for trend and seasonality modeling.

Robust to missing data and outliers; interpretable predictions with uncertainty intervals.

3. Model Training & Forecasting

Trained on historical monthly prices.

Forecasts generated for the next 12 months.

4.Model Evaluation

Metrics: MAE (Mean Absolute Error), RMSE (Root Mean Squared Error).

Compared last 12 months of historical data vs predicted prices to validate performance.


Business Insights ::

Predicted Price Increase:

Increase inventory, negotiate contracts early, adjust pricing.

Predicted Price Decrease:

Delay procurement, offer promotions, reduce inventory.

Effectiveness Evaluation:

Track actual prices vs forecasted prices.

Monitor KPIs: profit margin, stock turnover, cost savings.

Retrain model if consistent deviations are observed.



Deployment :

Framework: Django-based web application for real-time predictions.

Integration:

Save trained model using pickle.

Accept CSV uploads or user input via web forms.

Display forecasted prices and trend plots.

Monitoring:

Track MAE/RMSE monthly.

Detect model drift and retrain as needed.

Maintain model versioning for rollback.


Installation & Usage :

Clone the Repository
git clone https://github.com/BabuShaik778/Monthly-Price-Forecasting.git
cd Monthly-Price-Forecasting

Install Dependencies :
pip install -r requirements.txt

python manage.py runserver

Access the Application

Open your browser and navigate to:

http://127.0.0.1:8000/

Use the App :

Upload the CSV with historical monthly prices
OR
Enter required inputs using the web interface

The app will show the 12-month price forecast with visualization.

