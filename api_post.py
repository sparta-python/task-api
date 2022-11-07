import requests


url = "http://127.0.0.1:5000/post"

data = {"name": "Jun"}

res = requests.post(url, json=data)

JSON_object = res.json()

print(JSON_object)
