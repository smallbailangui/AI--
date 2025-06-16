# Please install OpenAI SDK first: `pip3 install openai`
# sk-hrfqruxzhkwhwwjpahpivsmflxiskxrzqtxejhqvrymmejqc 第三方申请的api密钥(用不了)
# sk-0ecf5c29fc6d4dab80206021fb14a384 deepseek官方申请的api
from openai import OpenAI # type: ignore

client = OpenAI(api_key="sk-hrfqruxzhkwhwwjpahpivsmflxiskxrzqtxejhqvrymmejqc", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)