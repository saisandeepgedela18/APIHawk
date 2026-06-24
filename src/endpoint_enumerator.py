import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

endpoints = [
    "/users",
    "/posts",
    "/comments",
    "/albums",
    "/todos"
]

print("=" * 50)
print("APIHAWK ENDPOINT ENUMERATION")
print("=" * 50)

for endpoint in endpoints:
    url = BASE_URL + endpoint

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{endpoint} --> ACTIVE")
        else:
            print(f"{endpoint} --> INACTIVE")

    except:
        print(f"{endpoint} --> ERROR")