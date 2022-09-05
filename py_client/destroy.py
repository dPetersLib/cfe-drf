import requests
import json

endpoint = 'http://localhost:8000/products/5/delete/'

response = requests.delete(endpoint)

print(response.status_code)
