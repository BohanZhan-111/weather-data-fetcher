"""
Week 3 练习项目：Open-Meteo API 数据抓取

运行方式：
1. 立即运行一次：python main.py
2. 指定城市运行：python main.py --city Boston
3. 启动定时任务：python main.py --schedule
"""

import argparse
import time
from datetime import datetime
from typing import Optional

import requests
import schedule

from config import DATA_DIR, DEFAULT_CITY, SCHEDULE_TIME, WEATHER_CSV_PATH
from geocoding import get_city_location
from weather import fetch_weather


def fetch_all(city: Optional[str] = None):
    """主流程：城市名 -> 经纬度 -> 天气 DataFrame -> 保存 CSV。"""
    if city is None:
        city = DEFAULT_CITY

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'=' * 50}")
    print(f"开始抓取 Open-Meteo 天气 | {timestamp}")
    print(f"城市：{city}")
    print(f"{'=' * 50}")

    try:
        location = get_city_location(city)
        if location is None:
            return None

        print(
            f"City: {location['city']}, {location['country']} "
            f"({location['latitude']}, {location['longitude']})"
        )

        df_weather = fetch_weather(location)

        DATA_DIR.mkdir(exist_ok=True)
        df_weather.to_csv(WEATHER_CSV_PATH, index=False)

        print(f"\n数据已保存到 {WEATHER_CSV_PATH} ✓")
        print(df_weather)
        return df_weather

    except requests.exceptions.RequestException as e:
        print(f"[错误] 网络请求失败: {e}")
        return None
    except KeyError as e:
        print(f"[错误] JSON 字段不存在，请检查 API 参数或返回内容: {e}")
        return None
    except Exception as e:
        print(f"[错误] 未知错误: {e}")
        return None


def run_scheduler(city: Optional[str] = None) -> None:
    """每天固定时间自动抓取一次天气。"""
    schedule.every().day.at(SCHEDULE_TIME).do(fetch_all, city=city)

    print(f"定时任务已启动：每天 {SCHEDULE_TIME} 抓取一次天气。Ctrl+C 退出。")
    while True:
        schedule.run_pending()
        time.sleep(60)


def main() -> None:
    parser = argparse.ArgumentParser(description="Week 3 Open-Meteo API project")
    parser.add_argument("--city", type=str, help="指定城市，例如 Boston")
    parser.add_argument("--schedule", action="store_true", help="启动定时任务")
    args = parser.parse_args()

    if args.schedule:
        fetch_all(city=args.city)
        run_scheduler(city=args.city)
    else:
        fetch_all(city=args.city)


if __name__ == "__main__":
    main()
