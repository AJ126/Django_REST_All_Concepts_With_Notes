import requests

base_url = "http://127.0.0.1:8000/"
endpoint = "firstapi/customers"
print('Testing GET request to endpoint:', base_url + endpoint)
r = requests.get(base_url + endpoint)
print(r.status_code)
data = r.json()
print(data)