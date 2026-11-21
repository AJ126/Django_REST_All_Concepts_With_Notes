
import requests

base_url = 'http://localhost:8000'
end_point = 'serializationapi/detailview'

url = f"{base_url}/{end_point}"
print('url.......', url)

operation = input("Enter operation (GET/POST/PUT/DELETE): ").upper()

while operation not in ["GET", "POST", "PUT", "DELETE"]:
    print("Invalid operation. Please enter a valid operation.")
    exist = input("Do you want to continue? (y/n): ").lower()
    if exist == "n":
        print("Exiting the program.")
        exit()
    operation = input("Enter operation (GET/POST/PUT/DELETE): ").upper()

# GET records
if operation == 'GET':
    id = input("Enter ID (leave blank for all): ")
    if id != "":
        response = requests.get(url, params={'id': id})
    else:
        response = requests.get(url)
    print('response..........', response)
    print(response.status_code)
    print(response.json())

# POST record
elif operation == 'POST':
    data = {
        "name": input("Enter name: "),
        "info": input("Enter information: "),
        "phone": input("Enter phone: ")
    }
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())

# PUT record
elif operation == 'PUT':
    id = input("Enter ID to update: ")
    data = {
        "id": id,
        "name": input("Enter name: "),
        "info": input("Enter information: "),
        "phone": input("Enter phone: ")
    }
    response = requests.put(url, json=data)
    print(response.status_code)
    print(response.json())

# DELETE record
elif operation == 'DELETE':
    id = input("Enter ID to delete: ")
    response = requests.delete(url, params={'id': id})
    print(response.status_code)
    print(response.json())
