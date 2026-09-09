import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url, timeout=10)

data = response.json()

print("Status code:", response.status_code)
print("Title:", data["title"])
print("Completed:", data["completed"])
print("Python type:", type(data))