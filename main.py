import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPENWEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
app_key = os.getenv("APPID")

weather_params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": app_key,
    "cnt": 4
}

data = requests.get(url=OPENWEATHER_ENDPOINT, params=weather_params)

weather_data= data.json()

will_rain = False

for hour_data in weather_data["list"]:
    #print(hour_data["weather"][0])
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
