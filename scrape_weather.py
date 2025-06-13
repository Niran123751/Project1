import requests

def get_weather(city):
    try:
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
        response = requests.get(url, params=params)
        loc_data = response.json()

        # SAFETY CHECK: City not found
        results = loc_data.get("response", {}).get("results", [])
        if not results:
            return {"error": f"City '{city}' not found in BBC location API."}

        location_id = results[0]["id"]
        weather_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"
        weather_data = requests.get(weather_url).json()
        forecast = weather_data.get("forecasts", {}).get("today", {})

        if not forecast:
            return {"error": f"No forecast data found for city '{city}'."}

        return {
            "city": city,
            "temperature_min": forecast.get("min_temp"),
            "temperature_max": forecast.get("max_temp"),
            "summary": forecast.get("summary")
        }

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
