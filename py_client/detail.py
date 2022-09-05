import requests
import json

endpoint = 'http://localhost:8000/products/1/'

response = requests.get(endpoint)

print(response.json())
print(response.status_code)
