"""
经纬度 -> 天气 DataFrame
使用 Open-Meteo Forecast API。
"""

import pandas as pd
import requests

from config import FORECAST_URL


def fetch_weather(location: dict) -> pd.DataFrame:
    """根据 location 字典获取未来 7 天天气，并整理成 DataFrame。"""
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
        "forecast_days": 7,
    }

    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    daily = data["daily"]
    df = pd.DataFrame({
        "city": location["city"],
        "country": location["country"],
        "date": daily["time"],
        "temperature_max_c": daily["temperature_2m_max"],
        "temperature_min_c": daily["temperature_2m_min"],
        "precipitation_probability_max_percent": daily["precipitation_probability_max"],
    })

    print(f"[weather] 获取 {location['city']} 未来 {len(df)} 天预报 ✓")
    return df
