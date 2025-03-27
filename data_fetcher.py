import requests
import time
from config import API_KEY, logger

def fetch_weather_data(location, retries=3, delay=5):
    """Fetches weather data from OpenWeather API with retry mechanism."""
    if not API_KEY:
        logger.error("API key is missing! Check your .env file.")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt}/{retries} failed: {e}")
            time.sleep(delay)

    logger.error(f"All {retries} attempts to fetch weather data failed.")
    return None
