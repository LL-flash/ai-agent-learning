from tools.weather import get_weather
from tools.calculator import calculate


TOOLS = {
    "weather": get_weather,
    "calculator": calculate,
}


TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, like Tokyo or Berlin",
                    },
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a math expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression, like 2+3*4",
                    },
                },
                "required": ["expression"],
            },
        },
    },
]
