from tools.weather import get_weather
from tools.calculator import calculate


TOOLS = {
    "weather": get_weather,
    "calculator": calculate,
}


TOOLS_SCHEMA = [
    {
        "name": "weather",
        "description": "Get weather for a city",
        "parameters": {
            "city": "string",
        },
    },
    {
        "name": "calculator",
        "description": "Calculate a math expression",
        "parameters": {
            "expression": "string",
        },
    },
]