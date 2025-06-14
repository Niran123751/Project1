import requests
import traceback

def get_weather(city):
    try:
        # 1. Get city location ID from BBC API
        url = "https://locator-service.api.bbci.co.uk/locations"
        params = {
            "api_key": "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv",
            "stack": "aws",
            "locale": "en",
            "filter": "international",
            "place-types": "settlement,airport,district",
            "order": "importance",
            "s": city,
            "a": "true",
            "format": "json"
        }

        res = requests.get(url, params=params, timeout=5)
        loc_data = res.json()
        print("Location API response:", loc_data)

        results = loc_data.get("response", {}).get("results", [])
        print("results type:", type(results), results)

        if isinstance(results, list) and results:
            location_id = results[0].get("id")
        else:
            return {"error": f"No valid location found for '{city}'."}

        # 2. Get weather forecast for the location ID
        weather_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"
        weather_data = requests.get(weather_url, timeout=5).json()
        print("Weather API response:", weather_data)

        forecast = weather_data.get("forecasts", {}).get("today", {})
        if not forecast:
            return {"error": "No forecast data found."}

        return {
            "city": city,
            "temperature_min": forecast.get("min_temp"),
            "temperature_max": forecast.get("max_temp"),
            "summary": forecast.get("summary")
        }

    except Exception:
        print("ERROR occurred:")
        print(traceback.format_exc())
        return {"error": "Internal server error. Check logs for details."}
