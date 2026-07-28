def get_weather(city):

    weather_data = {
        "Tokyo": "rainy",
        "Berlin": "cloudy",
        "Beijing": "sunny",
        "London": "windy"
    }

    condition = weather_data.get(
        city,
        "unknown"
    )

    return f"The weather in {city} is {condition}"