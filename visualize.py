"""Charting utilities for the weather forecast project."""

import pandas as pd
from matplotlib import pyplot as plt


def save_temperature_chart(df: pd.DataFrame, output_path) -> None:
    """Save a temperature forecast line chart as a PNG file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    chart_df = df.copy()
    chart_df["date"] = pd.to_datetime(chart_df["date"])

    plt.figure(figsize=(10, 5))
    plt.plot(chart_df["date"], chart_df["temperature_max_c"], marker="o", label="Max temp (°C)")
    plt.plot(chart_df["date"], chart_df["temperature_min_c"], marker="o", label="Min temp (°C)")
    plt.title(f"7-Day Temperature Forecast: {chart_df['city'].iloc[0]}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
