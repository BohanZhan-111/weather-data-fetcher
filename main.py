"""Command-line entry point for the Week 3 Open-Meteo weather data project."""

import argparse
import logging
import time
from datetime import datetime
from typing import Optional

import requests
import schedule

from config import (
    CHARTS_DIR,
    DATA_DIR,
    DEFAULT_CITY,
    LOG_FILE_PATH,
    LOGS_DIR,
    SCHEDULE_TIME,
    WEATHER_CHART_PATH,
    WEATHER_CSV_PATH,
)
from geocoding import get_city_location
from visualize import save_temperature_chart
from weather import fetch_weather


def setup_logging() -> None:
    """Configure console and file logging."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def fetch_all(city: Optional[str] = None):
    """Run the full pipeline: geocode city, fetch weather, save CSV, and save chart."""
    selected_city = city or DEFAULT_CITY
    started_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logging.info("Starting weather pipeline at %s", started_at)
    logging.info("Selected city: %s", selected_city)

    try:
        location = get_city_location(selected_city)
        if location is None:
            logging.warning("City not found: %s", selected_city)
            return None

        logging.info(
            "Resolved location: %s, %s (%s, %s)",
            location["city"],
            location["country"],
            location["latitude"],
            location["longitude"],
        )

        df_weather = fetch_weather(location)

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        CHARTS_DIR.mkdir(parents=True, exist_ok=True)

        df_weather.to_csv(WEATHER_CSV_PATH, index=False)
        save_temperature_chart(df_weather, WEATHER_CHART_PATH)

        logging.info("Saved CSV file: %s", WEATHER_CSV_PATH)
        logging.info("Saved chart file: %s", WEATHER_CHART_PATH)
        logging.info("Pipeline finished successfully")

        print(df_weather)
        return df_weather

    except requests.exceptions.RequestException as error:
        logging.exception("Network or API request failed: %s", error)
        return None
    except KeyError as error:
        logging.exception("Unexpected API response structure. Missing key: %s", error)
        return None
    except Exception as error:
        logging.exception("Unexpected error: %s", error)
        return None


def run_scheduler(city: Optional[str] = None, test_mode: bool = False) -> None:
    """Run the pipeline on a schedule."""
    if test_mode:
        schedule.every(10).seconds.do(fetch_all, city=city)
        logging.info("Test scheduler started: running every 10 seconds")
    else:
        schedule.every().day.at(SCHEDULE_TIME).do(fetch_all, city=city)
        logging.info("Daily scheduler started: running every day at %s", SCHEDULE_TIME)

    logging.info("Press Ctrl+C to stop the scheduler")
    while True:
        schedule.run_pending()
        time.sleep(1 if test_mode else 60)


def main() -> None:
    """Parse command-line arguments and run the selected mode."""
    parser = argparse.ArgumentParser(description="Open-Meteo weather data fetcher")
    parser.add_argument("--city", type=str, help="City name, for example: Boston")
    parser.add_argument("--schedule", action="store_true", help="Run the daily scheduler")
    parser.add_argument(
        "--test-schedule",
        action="store_true",
        help="Run the scheduler every 10 seconds for testing",
    )
    args = parser.parse_args()

    setup_logging()

    if args.schedule:
        fetch_all(city=args.city)
        run_scheduler(city=args.city)
    elif args.test_schedule:
        fetch_all(city=args.city)
        run_scheduler(city=args.city, test_mode=True)
    else:
        fetch_all(city=args.city)


if __name__ == "__main__":
    main()
