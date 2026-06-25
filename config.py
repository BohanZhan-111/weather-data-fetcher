"""
项目配置：集中读取 .env 里的默认值。

Open-Meteo 不需要 API Key，所以这里主要用 .env 练习保存默认城市、定时时间等配置。
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
WEATHER_CSV_PATH = DATA_DIR / os.getenv("WEATHER_CSV_NAME", "weather.csv")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Boston")
SCHEDULE_TIME = os.getenv("SCHEDULE_TIME", "09:00")

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
