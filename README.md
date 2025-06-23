# End-to-End-ETL-Pipeline-Project-using-docker
ETL pipeline using Docker, Python, Airflow, PostgreSQL, and DBT. Extracts data from an API, stores raw data in PostgreSQL, transforms it in DBT (staging and marts), and schedules everything using Airflow. Containerized and modular for easy deployment.

# ETL Pipeline with Docker, Airflow, PostgreSQL, DBT, and Python

This project builds a complete ETL pipeline using:

    Docker for containerization

    Airflow to orchestrate tasks

    PostgreSQL as the database

    DBT for transformations

    Python for data extraction and custom logic

Pipeline Workflow

    Extracts data from a public API using Python

    Saves raw data into PostgreSQL

    Transforms data in a staging layer with DBT

    Builds final data marts for analysis

    Automates all steps using Airflow

Features

    Fully containerized with Docker Compose

    Python scripts for flexible API integration

    SQL transformations versioned in DBT

    Automated scheduling and retries with Airflow

Structure

    extract/: Python scripts for API ingestion

    airflow/: DAGs and configuration

    dbt/: Models for staging and marts

    docker-compose.yml: Orchestration config

Tools Used

    Python 3.12.3

    Apache Airflow

    PostgreSQL

    DBT

    Docker + Docker Compose
