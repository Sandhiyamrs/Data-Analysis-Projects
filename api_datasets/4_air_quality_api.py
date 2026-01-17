import requests

API_KEY = "YOUR_API_KEY"
CITY = "Delhi"
URL = "https://api.openweathermap.org/data/2.5/air_pollution"

def fetch_air_quality(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()

    air_data = data["list"][0]["components"]
    air_data["aqi"] = data["list"][0]["main"]["aqi"]
    return air_data

if __name__ == "__main__":
    # Example coordinates for Delhi
    air_quality = fetch_air_quality(28.6139, 77.2090)
    print(air_quality)
