import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

print("DeepSeek API key loaded:", api_key is not None)