import json

# Load Swagger JSON
with open("datasets/swagger.json", "r") as file:
    swagger = json.load(file)

print("=" * 50)
print("APIHAWK SWAGGER PARSER")
print("=" * 50)

print("\nDocumented APIs:\n")

for endpoint in swagger["paths"]:
    print(endpoint)