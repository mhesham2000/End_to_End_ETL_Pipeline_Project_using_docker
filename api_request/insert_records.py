import psycopg2
from api_request import mock_fetch_data, fetch_data


def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password")
        print("Connected to the database successfully.")
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise
    
    
def create_table(conn):
    print("Creating table if it does not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev ;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                uct_offset FLOAT
            );
        """)
        conn.commit()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        conn.rollback()
        raise

def insert_data(conn, data):
    print("Inserting data into the table...")
    try:

        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, time, uct_offset)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING *;
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        inserted_row = cursor.fetchone()

        conn.commit()
        print("Data inserted successfully.")
        print("Inserted row:", inserted_row)
    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")
        conn.rollback()
        raise
def Insert_record_from_api_to_db():
    try:
        print("Starting the process to insert records from API to database...")
        conn = connect_to_db()
        create_table(conn)
        insert_data(conn,mock_fetch_data())
        print("Data inserted successfully.")
    except Exception as e:  
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")
            
# Insert_record_from_api_to_db()