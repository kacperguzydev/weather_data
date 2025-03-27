from data_fetcher import fetch_weather_data
from data_processor import process_weather_data
from data_storage import store_weather_data
from config import logger


def main():
    location = "Katowice"  # Change as needed

    logger.info(f"Fetching weather data for {location}...")
    weather_data = fetch_weather_data(location)

    if not weather_data:
        logger.error("Failed to fetch weather data. Exiting.")
        return

    processed_data = process_weather_data(weather_data)

    if processed_data:
        store_weather_data(processed_data)
        logger.info("Weather data successfully stored.")
    else:
        logger.warning("No valid weather data to store.")


if __name__ == "__main__":
    main()
