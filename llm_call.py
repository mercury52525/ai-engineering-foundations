import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "user",
            "content": "用一句话解释什么是 API。"
        }
    ],
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)

print("Content:", response.choices[0].message.content)
print("Finish reason:", response.choices[0].finish_reason)
print("Model:", response.model)

print("Prompt tokens:", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)