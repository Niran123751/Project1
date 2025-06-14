import os
import traceback
import requests
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

def get_weather(city):
    try:
        api_key = os.getenv("OWM_API_KEY")
        if not api_key:
            return {"error": "API key not configured."}

        # 1. Get coordinates using Geocoding API
        loc_resp = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct",
            params={"q": city, "limit": 1, "appid": api_key},
            timeout=5
        )
        loc_resp.raise_for_status()
        loc_data = loc_resp.json()
        print("Geocoding response:", loc_data)

        if not loc_data:
            return {"error": f"City '{city}' not found."}

        lat, lon = loc_data[0]["lat"], loc_data[0]["lon"]

        # 2. Get current weather
        weather_resp = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric"},
            timeout=5
        )
        weather_resp.raise_for_status()
        data = weather_resp.json()
        print("Weather response:", data)

        main = data.get("main", {})
        weather_desc = data.get("weather", [{}])[0].get("description", "")

        return {
            "city": city,
            "temperature": main.get("temp"),
            "feels_like": main.get("feels_like"),
            "weather": weather_desc
        }

    except Exception:
        print("ERROR occurred:\n", traceback.format_exc())
        return {"error": "Internal server error. Check logs for details."}

