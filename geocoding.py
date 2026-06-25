"""
城市名 -> 经纬度
使用 Open-Meteo Geocoding API。
"""

from typing import Optional

import requests

from config import GEOCODING_URL


def get_city_location(city: str) -> Optional[dict]:
    """用城市名查询经纬度、国家、时区。"""
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data.get("results"):
            print(f"找不到城市：{city}")
            return None

        result = data["results"][0]
        return {
            "city": result["name"],
            "country": result.get("country", ""),
            "latitude": result["latitude"],
            "longitude": result["longitude"],
            "timezone": result.get("timezone", "auto"),
        }

    except requests.exceptions.Timeout:
        print("Geocoding request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Geocoding request failed: {e}")
        return None
