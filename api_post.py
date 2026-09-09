import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Phase 1 API practice",
    "body": "This is my first POST request.",
    "userId": 1
}

response = requests.post(url, json=payload, timeout=10)

print("Status code:", response.status_code)
print("Response JSON:", response.json())

print("Request method:", response.request.method)
print("Request URL:", response.request.url)
print("Content-Type:", response.request.headers["Content-Type"])
print("Request body:", response.request.body)