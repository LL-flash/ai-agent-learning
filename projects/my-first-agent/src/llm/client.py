import os
import json

from openai import OpenAI
from dotenv import load_dotenv


class LLMClient:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("DEEPSEEK_API_KEY")

        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found")


        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

        print("DeepSeek client initialized")


    def chat(self, prompt):

        response = self.client.chat.completions.create(
            model="deepseek-chat",

            response_format={
                "type": "json_object"
            },

            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI agent planner.

Your job is to decide which tool to use.

Available tools:

weather(city)

Return JSON only.

Example:

{
    "tool": "weather",
    "city": "Tokyo"
}
"""
                },

                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        content = response.choices[0].message.content

        return json.loads(content)