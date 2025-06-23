import requests
import time

api_key = "4c8a4d7f5ab2c87c7aca559c712ed48e"
city = "cairo"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"

def fetch_data():
    print("Fetching weather data from the API...")
    try:
        respond = requests.get(api_url)
        respond.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)         
        print("Data fetched successfully.")
        time.sleep(6)  
    
        return respond.json()
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise



# fetch_data()


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Cairo, Egypt', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Cairo', 'country': 'Egypt', 'region': 'Al Qahirah', 'lat': '30.050', 'lon': '31.250', 'timezone_id': 'Africa/Cairo', 'localtime': '2025-06-21 23:58', 'localtime_epoch': 1750550280, 'utc_offset': '3.0'}, 'current': {'observation_time': '08:58 PM', 'temperature': 28, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '04:54 AM', 'sunset': '06:59 PM', 'moonrise': '01:07 AM', 'moonset': '02:47 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 26}, 'air_quality': {'co': '381.1', 'no2': '29.23', 'o3': '100', 'so2': '69.005', 'pm2_5': '29.6', 'pm10': '43.475', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 22, 'wind_degree': 333, 'wind_dir': 'NNW', 'pressure': 1012, 'precip': 0, 'humidity': 45, 'cloudcover': 0, 'feelslike': 28, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}