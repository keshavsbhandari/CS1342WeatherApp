# weather_app_realtime/data/fetch.py

import requests

API_KEY = "18559c9e27cd41d6bd4165313252910"
# How to get an API Key
# Step 1: Signup @: https://www.weatherapi.com/
# Step 2: Verify your email (Click the link you get after signup)
# Step 3: Login back to https://www.weatherapi.com/
# Step 4: Once logged in you will see API key, copy this and replace it in above line3
# Note: This will expire soon
# More: If you click TOOLS API EXPLORER ON LEFT SIDE, YOU CAN ACCESS THE EXPLORER AND CLICK WEATHER API DOCUMENTATION FOR MORE DETAIL
# WEATHER API DOCS: https://www.weatherapi.com/docs/, if you scroll all the way down you will see "Example response of alerts"

def fetch_weather_data(zip_codes):
    """
    Fetches real-time weather data for multiple ZIP codes using WeatherAPI.com's bulk feature.

    Args:
    zip_codes (list): A list of ZIP codes as strings.

    Returns:
    dict: A dictionary containing detailed weather information for each ZIP code.
    
    
    """
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=bulk"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "locations": [{"q": zip_code, "custom_id": f"zip-{zip_code}"} for zip_code in zip_codes]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        weather_data = response.json()
    else:
        weather_data = {"error": "Unable to fetch data"}

    return weather_data