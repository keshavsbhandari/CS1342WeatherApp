# view/format.py
from data.fetch import fetch_weather_data
from data.process import process_weather_data

def format_weather_data(weather_data):
    # Fetch weather information for a single ZIP code
    # weather_data = fetch_weather_data([zip_code.strip() for zip_code in zip_codes.split(',')])
    # weather_data = process_weather_data(weather_data)
    if "error" in weather_data:
        return "Error fetching data."

    # Extract the weather details
    formatted_data = []
    for zip_code, weather in weather_data.items():
        
        location = weather.get("location")
        current = weather.get("current")
        if location and current:
            # Format the weather information
            formatted_data.append(
                f"Location: {location['name']}, {location['region']}, {location['country']}\n"
                f"Temperature: {current['temperature_c']}°C ({current['temperature_f']}°F)\n"
                f"Condition: {current['condition']}\n"
                f"Humidity: {current['humidity']}%\n"
                f"Wind: {current['wind_mph']} mph / {current['wind_kph']} kph\n"
                f"Feels Like: {current['feelslike_c']}°C ({current['feelslike_f']}°F)\n"
                f"UV Index: {current['uv_index']}\n"
                f"Visibility: {current['visibility_km']} km / {current['visibility_miles']} miles\n"
                f"Local Time: {location['localtime']}"
            )
        else:
            formatted_data.append(f"No data available for the provided ZIP code = {zip_code}.")
    joiner = "\n" + "-"*100 + "\n"
    formatted_data = joiner.join(formatted_data)
    return formatted_data