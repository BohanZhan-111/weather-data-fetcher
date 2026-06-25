"""Weather API and DataFrame transformation helpers."""

import pandas as pd
import requests

from config import FORECAST_URL


def fetch_weather(location: dict) -> pd.DataFrame:
    """Fetch a 7-day weather forecast and return it as a pandas DataFrame."""
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
        "forecast_days": 7,
    }

    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    daily = response.json()["daily"]

    return pd.DataFrame(
        {
            "city": location["city"],
            "country": location["country"],
            "date": daily["time"],
            "temperature_max_c": daily["temperature_2m_max"],
            "temperature_min_c": daily["temperature_2m_min"],
            "precipitation_probability_max_percent": daily[
                "precipitation_probability_max"
            ],
        }
    )
