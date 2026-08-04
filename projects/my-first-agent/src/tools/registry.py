from tools.weather import get_weather
from tools.calculator import calculate
from tools.text_length import text_length

TOOLS = {
    "weather": get_weather,
    "calculator": calculate,
    "text_length": text_length,
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
    {
        "type": "function",
        "function": {
            "name": "text_length",
            "description": "Count the number of characters in a text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to count characters for.",
                    },
                },
                "required": ["text"],
            },
        },
    },
]
