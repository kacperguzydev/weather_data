from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine
import pandas as pd
from config import DATABASE_URI

app = FastAPI(title="Weather Data API", version="1.0")
engine = create_engine(DATABASE_URI)


@app.get("/")
def root():
    return {"message": "Welcome to the Weather API. Use /weather to get stored weather data."}


@app.get("/weather")
def get_weather_data(location: str, limit: int = Query(10, ge=1, le=100)):
    """Fetches stored weather data from PostgreSQL."""
    query = f"SELECT * FROM weather_data WHERE location='{location}' ORDER BY timestamp DESC LIMIT {limit}"

    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    if df.empty:
        raise HTTPException(status_code=404, detail="No weather data found for the given location.")

    return df.to_dict(orient="records")
