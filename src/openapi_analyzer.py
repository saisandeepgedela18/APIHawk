import json

with open("datasets/swagger.json", "r") as file:
    data = json.load(file)

print("=" * 50)
print("APIHAWK OPENAPI ANALYZER")
print("=" * 50)

print(f"API Title   : {data['info']['title']}")
print(f"Version     : {data['info']['version']}")

paths = data["paths"]

print(f"\nTotal Endpoints : {len(paths)}")

print("\nAvailable Endpoints:\n")

for endpoint in paths:
    methods = ", ".join(paths[endpoint].keys()).upper()
    print(f"{methods:<10} {endpoint}")