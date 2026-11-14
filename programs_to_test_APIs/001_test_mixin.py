import requests

base_url = "http://127.0.0.1:8000/"
endpoint = "mixinsapi/infotest/"
id = int(input('Which id to test?:'))
url = f"{base_url}{endpoint}{id}/"
r = requests.get(url)
print(r.status_code)
data = r.json()
print(data)