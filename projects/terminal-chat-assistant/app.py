import os
from dotenv import load_dotenv
from openai import OpenAI


# 加载环境变量
load_dotenv()


# 创建 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


messages = []

while True:

    

    user_input = input("你: ")

    if user_input.strip() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        print("AI:")
        print(ai_reply)

        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

    except Exception as e:
        print("发生错误:")
        print(e)