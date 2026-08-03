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


    def chat(self, messages):

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            response_format={
                "type": "json_object"
            },
            messages=messages
        )

        content = response.choices[0].message.content

        return json.loads(content)


    def create_message(self, messages, tools=None):
        request = {
            "model": "deepseek-chat",
            "messages": messages,
        }

        if tools is not None:
            request["tools"] = tools

        response = self.client.chat.completions.create(**request)

        return response.choices[0].message
