import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Fetch configurations
API_KEY = os.getenv("WEATHER_API_KEY")
DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://postgres:1234@localhost:5432/weather")

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("WeatherPipeline")

# Ensure API key is set
if not API_KEY:
    logger.error("API key not found! Check your .env file.")
