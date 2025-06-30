# Weather Data ETL Pipeline

ETL pipeline that extracts weather data from a public API using Python, loads it into PostgreSQL, transforms it using DBT, and schedules everything with Airflow. Containerized using Docker.

---

![Image](https://github.com/user-attachments/assets/4e100ab5-9190-4c51-9475-1b36b3016321)

![Image](https://github.com/user-attachments/assets/7ae859b0-796e-4df4-bbee-0c7a21adf5f4)
![Image](https://github.com/user-attachments/assets/c96f840b-6722-4379-b23c-e6f2ecb476de)

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
```
## How to run
    docker compose up af
