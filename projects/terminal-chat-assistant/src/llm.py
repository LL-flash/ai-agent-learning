from openai import OpenAI
from config import  (DEEPSEEK_API_KEY,BASE_URL,)

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=BASE_URL,
)
