import requests

def get_weather(city):
    try:
        # Step 1: Get city location ID
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

        res = requests.get(url, params=params).json()
        results = res.get("response", {}).get("results", [])

        if not results:
            return {"error": f"City '{city}' not found."}

        location_id = results[0]["id"]

        # Step 2: Get weather forecast
        weather_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"
        weather_data = requests.get(weather_url).json()
        forecast = weather_data.get("forecasts", {}).get("today")

        if not forecast:
            return {"error": "No forecast data available."}

        return {
            "city": city,
            "temperature_min": forecast.get("min_temp"),
            "temperature_max": forecast.get("max_temp"),
            "summary": forecast.get("summary")
        }

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

