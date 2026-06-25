# Week 3 Open-Meteo API 项目

这个项目练习：

- `requests` 调用 API
- 解析 JSON
- 保存为 pandas DataFrame
- 使用 `.env` 管理配置
- 使用 `schedule` 做定时任务

## 项目结构

```text
week3_open_meteo_clean/
├── main.py             # 程序入口：运行抓取 / 定时任务
├── config.py           # 读取 .env 配置
├── geocoding.py        # 城市名 -> 经纬度
├── weather.py          # 经纬度 -> 天气 DataFrame
├── requirements.txt    # 依赖包
├── .env.example        # .env 模板
├── .gitignore          # 防止 .env / data CSV 被上传
├── data/               # 自动保存 weather.csv
└── README.md
```

## 1. 安装依赖

```bash
pip install -r requirements.txt
```

## 2. 配置 .env

Open-Meteo 不需要 API Key，所以 `.env` 主要用来练习保存默认城市和定时时间。

```bash
cp .env.example .env
```

`.env` 示例：

```env
DEFAULT_CITY=Boston
SCHEDULE_TIME=09:00
DATA_DIR=data
WEATHER_CSV_NAME=weather.csv
```

## 3. 立即运行一次

使用 `.env` 里的默认城市：

```bash
python main.py
```

指定城市：

```bash
python main.py --city "New York"
```

## 4. 启动定时任务

```bash
python main.py --schedule
```

程序会先抓取一次，然后每天按 `.env` 里的 `SCHEDULE_TIME` 自动抓取。

## 5. 输出结果

运行后会生成：

```text
data/weather.csv
```

里面包含：

- city
- country
- date
- temperature_max_c
- temperature_min_c
- precipitation_probability_max_percent

## 说明

这个版本只保留 Open-Meteo 部分，更符合你现在的 task。JSONPlaceholder 和 RestCountries 已经移除。
