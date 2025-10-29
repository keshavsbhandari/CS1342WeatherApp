# weather_app_realtime/data/process.py

def process_weather_data(weather_data):
    weather_reports = {}
    if "error" in weather_data:
        weather_reports['status'] = 'Error!!!'
        return weather_reports
    
    # View the output format here: https://www.weatherapi.com/docs/
    for entry in weather_data.get("bulk", []):
        query = entry.get("query", {})
        location = query.get("location", {})
        current = query.get("current", {})
        
        weather_reports[query.get("custom_id")] = {
            "location": {
                "name": location.get("name"),
                "region": location.get("region"),
                "country": location.get("country"),
                "lat": location.get("lat"),
                "lon": location.get("lon"),
                "localtime": location.get("localtime")
            },
            "current": {
                "temperature_c": current.get("temp_c"),
                "temperature_f": current.get("temp_f"),
                "condition": current.get("condition", {}).get("text"),
                "humidity": current.get("humidity"),
                "wind_mph": current.get("wind_mph"),
                "wind_kph": current.get("wind_kph"),
                "pressure_mb": current.get("pressure_mb"),
                "feelslike_c": current.get("feelslike_c"),
                "feelslike_f": current.get("feelslike_f"),
                "uv_index": current.get("uv"),
                "visibility_km": current.get("vis_km"),
                "visibility_miles": current.get("vis_miles"),
                "gust_mph": current.get("gust_mph"),
                "gust_kph": current.get("gust_kph")
            }
        }
    return weather_reports