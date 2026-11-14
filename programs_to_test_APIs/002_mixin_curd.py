import requests

base_url = "http://localhost:8000/"
endpoint = "mixinsapi/testInfoFormView/"

operation = str(input("Enter operation (GET/POST/PUT/DELETE): ")).upper()

while operation not in ["GET", "POST", "PUT", "DELETE"]:
    print("Invalid operation. Please enter a valid operation (GET/POST/PUT/DELETE).")
    exist = input("Do you want to continue? (y/n): ")
    if exist.lower() == "n":
        print("Exiting the program.")
        exit()
    operation = str(input("Enter operation (GET/POST/PUT/DELETE): ")).upper()


if operation == "GET":
    id = input("Enter ID (leave blank for all): ")
    print('id.....', id)
    if id is not None and id != "":
        response = requests.get(f"{base_url}{endpoint}{id}/")
    else:
        print('else.....')
        response = requests.get(f"{base_url}{endpoint}")
    print(response.json())

elif operation == "POST":
    data = {
        "name": input("Enter name: "),
        "phone": input("Enter phone: "),
        "address": input("Enter address: ")
    }
    response = requests.post(f"{base_url}{endpoint}", json=data)
    print(response.json()) 

elif operation == "PUT":
    id = input("Enter ID to update: ")
    data = {
        "name": input("Enter new name: "),
        "phone": input("Enter new phone: "),
        "address": input("Enter new address: ")
    }
    response = requests.put(f"{base_url}{endpoint}{id}/", json=data)
    print(response.json())

elif operation == "DELETE":
    id = input("Enter ID to delete: ")
    response = requests.delete(f"{base_url}{endpoint}{id}/")
    print(response.json())