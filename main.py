import requests

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"

data = {
    "model": "ai/smolllm2",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Please write 500 words about the fall of Rome."
        }
    ]
}

response = requests.post(url, json=data)
response.raise_for_status()

print(response.json()["choices"][0]["message"]["content"])