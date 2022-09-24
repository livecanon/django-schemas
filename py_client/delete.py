import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.delete(endpoint + "5")
# print(get_response)

print(get_response.status_code)
# print(get_response.status_code)
