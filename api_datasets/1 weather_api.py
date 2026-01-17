import requests

API_KEY = "YOUR_API_KEY"
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    weather_info = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
    return weather_info

if __name__ == "__main__":
    print(fetch_weather())
