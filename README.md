# Weather Data Fetcher

A Python weather data pipeline that retrieves a 7-day weather forecast from the Open-Meteo API, saves the data as a CSV file, and generates a temperature trend chart.

## Features

- Convert a city name into latitude and longitude using the Open-Meteo Geocoding API
- Retrieve a 7-day weather forecast from the Open-Meteo Forecast API
- Save weather data as a CSV file
- Generate a temperature forecast chart with Matplotlib
- Log the execution process
- Read configuration from `.env`
- Handle API failures with fallback sample data

## Project Structure

```text
weather-data-fetcher/
├── main.py
├── config.py
├── geocoding.py
├── weather.py
├── visualize.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   └── weather.csv
└── charts/
    └── weather_forecast.png
```

## Technologies

- Python 3
- Requests
- Pandas
- Matplotlib
- python-dotenv
- Logging
- Open-Meteo API

## Installation

```bash
git clone https://github.com/BohanZhan-111/weather-data-fetcher.git
cd weather-data-fetcher
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```text
CITY=Boston
```

## Usage

```bash
python main.py
```

or

```bash
python main.py --city "New York"
```

## Output

- `data/weather.csv`
- `charts/weather_forecast.png`

## Example Output

![Weather Forecast](charts/weather_forecast.png)

## Workflow

```text
User Input
     │
     ▼
Geocoding API
     │
     ▼
Forecast API
     │
     ▼
Pandas DataFrame
     │
     ├── CSV Export
     └── Visualization
```

## Sample Console Output

```text
INFO | Starting weather pipeline
INFO | Selected city: Boston
INFO | Resolved location: Boston, United States
INFO | Saved CSV file
INFO | Saved chart file
INFO | Pipeline finished successfully
```

## Future Improvements

- Scheduled weather collection
- SQLite database support
- FastAPI REST API
- GitHub Actions
- Docker

## Author

**Bohan Zhan**

GitHub: https://github.com/BohanZhan-111
