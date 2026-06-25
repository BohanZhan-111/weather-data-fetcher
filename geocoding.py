"""Geocoding helpers for converting a city name into latitude and longitude."""

from typing import Optional

import requests

from config import GEOCODING_URL


def get_city_location(city: str) -> Optional[dict]:
    """Return location metadata for a city using the Open-Meteo Geocoding API."""
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        return None

    result = data["results"][0]
    return {
        "city": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "timezone": result.get("timezone", "auto"),
    }
