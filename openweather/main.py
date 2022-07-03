import os

from dotenv import load_dotenv
import requests

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/"


def get_weather_by_city(city_name):
    r = requests.get(BASE_URL + f"weather?q={city_name}&appid={OPENWEATHER_API_KEY}")
    data = r.json()
    print(data)


get_weather_by_city("London")
