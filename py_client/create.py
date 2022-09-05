import requests
import json

endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "Canvas"
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)
