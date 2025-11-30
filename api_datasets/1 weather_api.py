import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=11.01&longitude=76.95&hourly=temperature_2m"

data = requests.get(url).json()

df = pd.DataFrame({
    'time': data['hourly']['time'],
    'temperature': data['hourly']['temperature_2m']
})

df.to_csv("weather.csv", index=False)
print("Weather data saved.")
