# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'), # 设置环境变量后此处间接访问apikey
    # api_key='sk-975783c3a4934192a6245f737670d217', # 直接设置apikey(不安全)
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个有用的助手"},
        {"role": "user", "content": "给我讲一个笑话"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)