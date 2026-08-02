# Netflix Data Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-1.38+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
</p>

A production-style Netflix analytics solution built with Python, SQLite, and Streamlit. The project validates, cleans, transforms, and visualizes the Netflix catalog to provide business-centric insight for content strategy, geographic growth, and genre performance.

## Project Overview
This project reads the raw Netflix title dataset from the local data folder, validates quality risks, cleans missing values and inconsistent fields, and builds a reusable analytics workflow. It covers ETL, SQL analysis, statistical summaries, chart exports, and an interactive dashboard for reporting and stakeholder review.

## Features
- Automated data loading and validation
- Duplicate removal and missing-value handling
- Standardization for countries, ratings, duration, and genres
- SQL database creation and query exports
- Statistical summaries for business interpretation
- More than 25 generated charts and interactive plots
- Streamlit dashboard with filters and KPI monitoring
- Business insight report generation
- Logging and robust error handling

## Folder Structure
```text
Netflix-Data-Analysis/
├── data/
│   ├── raw/
│   │   └── netflix_titles.csv
│   └── processed/
│       └── cleaned_netflix.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── loader.py
│   ├── cleaning.py
│   ├── preprocessing.py
│   ├── statistics.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── sql_analysis.py
│   ├── report_generator.py
│   └── utils.py
├── dashboard/
│   ├── app.py
│   ├── pages/
│   └── assets/
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── outputs/
│   ├── charts/
│   ├── reports/
│   ├── tables/
│   └── logs/
├── requirements.txt
├── README.md
├── main.py
├── .gitignore
├── LICENSE
└── netflix_titles.csv
```

## Installation
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
python main.py
streamlit run dashboard/app.py
```

## Tech Stack
- Python 3.12+
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- sqlite3
- streamlit
- pathlib
- logging
- typing

## Dashboard Screenshots
Placeholder screenshots can be added after local dashboard execution.

## SQL Examples
```sql
SELECT type, COUNT(*) AS titles
FROM netflix_titles
GROUP BY type
ORDER BY titles DESC;

SELECT country, COUNT(*) AS titles
FROM netflix_titles
GROUP BY country
ORDER BY titles DESC
LIMIT 10;
```

## Business Insights
- The largest content concentration lives in the US and India.
- Movies dominate the platform, but TV shows maintain strong strategic value in global markets.
- Genre mix indicates that drama, comedy, and international categories are the most important growth levers.
- Growth is strongest in recent years, showing sustained expansion of the catalog.

## Future Enhancements
- Add automated unit tests
- Introduce a CI validation pipeline
- Expand dashboard pages with deeper drill-downs
- Add predictive content planning features

## License
This project is distributed under the MIT License.
