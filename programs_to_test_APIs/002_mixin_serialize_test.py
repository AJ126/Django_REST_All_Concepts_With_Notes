import requests
base_url = "http://localhost:8000"
endpoint = "/mixinsapi/showinfo/"
response = requests.get(base_url + endpoint)
print(response.status_code)
print(response.json())