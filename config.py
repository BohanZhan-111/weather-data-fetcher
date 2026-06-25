"""Central configuration for the Open-Meteo weather data project."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load local environment variables from .env when the file exists.
# Open-Meteo does not require an API key, but .env is useful for default settings.
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
CHARTS_DIR = BASE_DIR / os.getenv("CHARTS_DIR", "charts")
LOGS_DIR = BASE_DIR / os.getenv("LOGS_DIR", "logs")

WEATHER_CSV_PATH = DATA_DIR / os.getenv("WEATHER_CSV_NAME", "weather.csv")
WEATHER_CHART_PATH = CHARTS_DIR / os.getenv("WEATHER_CHART_NAME", "weather_forecast.png")
LOG_FILE_PATH = LOGS_DIR / os.getenv("LOG_FILE_NAME", "app.log")

DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Boston")
SCHEDULE_TIME = os.getenv("SCHEDULE_TIME", "09:00")

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
