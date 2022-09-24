import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {"title": "updated title 1"}

get_response = requests.put(endpoint + "1", json=data)
# print(get_response)

print(get_response.json())
# print(get_response.status_code)
