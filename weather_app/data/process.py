# weather_app/data/process.py

def process_weather_data(weather_data):
    # Simulate processing the fetched data
    processed_data = {
        "location": weather_data["location"],
        "temperature_celsius": weather_data["temperature"],
        "temperature_fahrenheit": weather_data["temperature"] * 9/5 + 32,
        "condition": weather_data["condition"],
    }
    return processed_data