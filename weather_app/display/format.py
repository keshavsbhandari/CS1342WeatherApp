# weather_app/display/format.py

def format_weather_data(processed_data):
    # Format the weather data for display
    
    formatted_data = (
        f"Weather in {processed_data['location']}:\n"
        f"Condition: {processed_data['condition']}\n"
        f"Temperature: {processed_data['temperature_celsius']}°C / "
        f"{processed_data['temperature_fahrenheit']}°F"
    )
    return formatted_data