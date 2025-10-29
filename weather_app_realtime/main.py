# main.py

from data.fetch import fetch_weather_data
from data.process import process_weather_data
from display.format import format_weather_data
from display.show import display_weather

def main():
    zip_codes = ["78666", "78130"]
    weather_data = fetch_weather_data(zip_codes)
    processed_data = process_weather_data(weather_data)
    formatted_data = format_weather_data(processed_data)
    display_weather(formatted_data)

if __name__ == "__main__":
    main()