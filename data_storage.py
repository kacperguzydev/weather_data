import pandas as pd
from sqlalchemy import create_engine, text
from config import DATABASE_URI, logger

def get_db_connection():
    """Creates and returns a database connection."""
    return create_engine(DATABASE_URI)

def store_weather_data(data):
    """Stores weather data in PostgreSQL, ensuring efficient inserts."""
    try:
        engine = get_db_connection()
        df = pd.DataFrame([data])

        with engine.begin() as connection:
            df.to_sql("weather_data", connection, if_exists="append", index=False, method="multi")

            # Log row count for verification
            count = connection.execute(text("SELECT COUNT(*) FROM weather_data")).scalar()
            logger.info(f"Total records in 'weather_data': {count}")

    except Exception as e:
        logger.error(f"Failed to store weather data: {e}")
