# Weather Data Fetcher

A Python project that fetches 7-day weather forecast data from the Open-Meteo API, stores the result as a CSV file, generates a temperature trend chart, and supports scheduled data collection.

This project was built as a Week 3 API practice project covering:

- `requests` for API calls
- JSON parsing
- `pandas` DataFrame transformation
- `.env` configuration with `python-dotenv`
- scheduled jobs with `schedule`
- logging
- chart generation with `matplotlib`
- Git and GitHub workflow

## Project Structure

```text
weather-data-fetcher/
├── main.py              # Command-line entry point
├── config.py            # Environment variables and project paths
├── geocoding.py         # City name to latitude/longitude
├── weather.py           # Open-Meteo forecast request and DataFrame creation
├── visualize.py         # Temperature chart generation
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment configuration
├── .gitignore           # Files that should not be committed
├── data/                # Generated CSV output
├── charts/              # Generated chart output
└── logs/                # Runtime logs
```

## API Used

| API | Purpose | API Key Required |
| --- | --- | --- |
| Open-Meteo Geocoding API | Convert a city name into latitude and longitude | No |
| Open-Meteo Forecast API | Fetch 7-day weather forecast data | No |

Open-Meteo does not require an API key, so this project uses `.env` for default project settings instead of secrets.

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If script execution is blocked, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the virtual environment again.

### 2. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Create a local `.env` file

```powershell
copy .env.example .env
```

You can edit `.env` to change the default city or schedule time:

```env
DEFAULT_CITY=Boston
SCHEDULE_TIME=09:00
```

## Usage

Run once with the default city from `.env`:

```powershell
python main.py
```

Run once with a specific city:

```powershell
python main.py --city Boston
```

Run the daily scheduler:

```powershell
python main.py --schedule
```

Run the test scheduler every 10 seconds:

```powershell
python main.py --test-schedule
```

Stop the scheduler with `Ctrl + C`.

## Output

After a successful run, the project creates:

```text
data/weather.csv
charts/weather_forecast.png
logs/app.log
```

The CSV contains:

- city
- country
- date
- maximum temperature in Celsius
- minimum temperature in Celsius
- maximum precipitation probability

## Example Workflow

```powershell
python main.py --city Boston
git add .
git commit -m "Upgrade weather data pipeline"
git push
```

## Notes

The `.env` file, virtual environment, logs, charts, and generated CSV files should not be committed to GitHub. The `.gitignore` file is configured to exclude them.
