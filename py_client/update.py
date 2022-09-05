import requests
import json

endpoint = 'http://localhost:8000/api/products/4/update/'

data = {
    "title": "Modified"
}

response = requests.put(endpoint, json=data)

print(response.json())
print(response.status_code)
