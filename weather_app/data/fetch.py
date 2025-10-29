# weather_app/data/fetch.py

import random

def fetch_weather_data(location):
    # Simulate fetching weather data for a location
    print(f"Fetching simulated weather data for {location}...")

    simulated_data = {
        "location": location,
        "temperature": random.randint(-10, 40),  # Simulate temperature between -10°C and 40°C
        "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"]),
    }

    return simulated_data