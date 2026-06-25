"""Weather API and DataFrame transformation helpers."""

from datetime import date, timedelta
import logging

import pandas as pd
import requests

from config import FORECAST_URL


def build_sample_weather(location: dict, days: int = 7) -> pd.DataFrame:
    """Build fallback sample weather data when the forecast API is unavailable."""
    today = date.today()
    rows = []

    for day_index in range(days):
        forecast_date = today + timedelta(days=day_index)
        temp_min = 16 + (day_index % 3)
        temp_max = temp_min + 7 + (day_index % 2)
        precipitation_probability = [20, 30, 45, 25, 15, 35, 40][day_index % 7]

        rows.append(
            {
                "city": location["city"],
                "country": location["country"],
                "date": forecast_date.isoformat(),
                "temperature_max_c": temp_max,
                "temperature_min_c": temp_min,
                "precipitation_probability_max_percent": precipitation_probability,
                "data_source": "sample_fallback",
            }
        )

    return pd.DataFrame(rows)


def fetch_weather(location: dict) -> pd.DataFrame:
    """Fetch a 7-day weather forecast and return it as a pandas DataFrame.

    If the forecast API is unavailable because of a timeout, connection reset,
    or other network issue, the function returns sample fallback data. This
    keeps the rest of the pipeline working so CSV export, chart generation,
    logging, and scheduling can still be tested.
    """
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
        "forecast_days": 7,
    }

    headers = {
        "User-Agent": "weather-data-fetcher/1.0"
    }

    try:
        response = requests.get(
            FORECAST_URL,
            params=params,
            headers=headers,
            timeout=(10, 30),
        )
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
                "data_source": "open_meteo_api",
            }
        )

    except requests.exceptions.RequestException as error:
        logging.warning(
            "Forecast API request failed: %s. Using sample fallback data instead.",
            error,
        )
        return build_sample_weather(location)
