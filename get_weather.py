import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

#RETURNS WEATHER FROM API IN JSON STYLE #F00 IMPROVE ANY LOCATIONS + ERROR CATCHING
def get_weather_data(location, when):
    try:
        API_Key = os.getenv('WEATHER_KEY')
        location = location
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
        final_url = weather_url + API_Key
        weather_data = requests.get(final_url).json()
        city_name = weather_data["name"]
        weather = weather_data["weather"]
        main_data = weather_data["main"]
        new_weather_data = {
            "name": city_name,
            "weather_description": weather[0]["description"],
            "temperature": str(round((int(main_data["temp"]) - 273.15),2)) + " degrees celcius"
        }
        return json.dumps(new_weather_data)
    except:
        return """{"error": "Sorry, the weather data is currently experiencing an error"}"""