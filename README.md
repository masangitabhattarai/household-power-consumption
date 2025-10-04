Household Power Consumption Forecasting
Project Overview

This project forecasts household electric power consumption using time series analysis.
The final model used is Facebook Prophet, chosen for its ability to capture daily and weekly seasonality patterns effectively.
The model is deployed using Streamlit, providing an interactive web interface for visualization and forecasting.
 Features

Real-time forecasting of household electricity usage.

Interactive Streamlit app for visualization and user input.

Displays historical trends, seasonality, and forecast intervals.

Shows residual plots and evaluation metrics (RMSE, MAE, MAPE).

Allows CSV download of forecasted results.

⚙️ Setup
Clone the Repository
git clone https://github.com/masangitabhattarai/household-power-consumption.git
cd household-power-consumption

Run the Streamlit App
streamlit run app.py
 Model Details

Final Model: Facebook Prophet

Forecast Range: 7 days ahead (hourly resolution)

Evaluation Metrics: RMSE, MAE, MAPE

Best Features: Captures trend and seasonality accurately

Performance: Outperformed ARIMA and Exponential Smoothing models

📸 Screenshots
<img width="1482" height="865" alt="image" src="https://github.com/user-attachments/assets/82bf6b5d-745b-49ad-bde3-ec5e5989971f" />
<img width="1288" height="573" alt="image" src="https://github.com/user-attachments/assets/b82ccc31-f5c6-42e0-ae59-e73f5cc088df" />
<img width="1326" height="488" alt="image" src="https://github.com/user-attachments/assets/dd3ea292-ff45-4784-85cf-2e6eff52fa0e" />
<img width="1239" height="685" alt="image" src="https://github.com/user-attachments/assets/136cd834-dd51-45c3-ac28-fe1237a4c1da" />

🔮 Future Enhancements

Add weather, temperature, and holiday data for improved accuracy.

Extend to monthly or yearly consumption forecasting.

Integrate with IoT-based real-time energy monitoring systems.

👩‍💻 Author

Sangita Bhattarai
📧 Email: masangitabhattarai@gmail.com

📞 Phone: 9863040642
📍 Location: Lalitpur, Nepal
