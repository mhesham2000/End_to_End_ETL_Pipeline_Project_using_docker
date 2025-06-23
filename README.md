# Weather Data ETL Pipeline

ETL pipeline that extracts weather data from a public API using Python, loads it into PostgreSQL, transforms it using DBT, and schedules everything with Airflow. Containerized using Docker.

---

## Features

- Extracts real-time weather data using Python
- Loads raw data into PostgreSQL
- Creates staging and data marts using DBT
- Orchestrated and scheduled by Apache Airflow
- Fully containerized and reproducible with Docker

---

## Architecture

```text
[Weather API] → [Python Script] → [PostgreSQL (raw)]
                                 ↓
                           [DBT Transformations]
                                 ↓
                        [PostgreSQL (data marts)]
                                 ↓
                             [Airflow DAGs]
