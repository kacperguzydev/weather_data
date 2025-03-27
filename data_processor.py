from config import logger

def process_weather_data(weather_data):
    """Extracts key weather details and ensures data integrity."""
    if not weather_data:
        logger.error("Received empty weather data.")
        return None

    try:
        return {
            "location": weather_data.get("name"),
            "temperature": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "weather_condition": weather_data["weather"][0]["description"]
        }
    except KeyError as e:
        logger.error(f"Missing data in API response: {e}")
        return None
