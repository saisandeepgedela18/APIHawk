import json

# Load documented APIs
with open("datasets/swagger.json", "r") as file:
    swagger = json.load(file)

documented = set(swagger["paths"].keys())

# Load active APIs
with open("logs/active_endpoints.txt", "r") as file:
    active = set(line.strip() for line in file if line.strip())

shadow = active - documented

print("=" * 60)
print("APIHAWK SECURITY REPORT")
print("=" * 60)

print(f"Documented APIs : {len(documented)}")
print(f"Active APIs     : {len(active)}")
print(f"Shadow APIs     : {len(shadow)}")

print("\nShadow API List")
print("-" * 30)

if shadow:
    for api in sorted(shadow):
        print(f"⚠ {api}")
else:
    print("No Shadow APIs Found")

print("\nOverall Risk Assessment")
print("-" * 30)

if len(shadow) == 0:
    print("LOW RISK")
elif len(shadow) <= 2:
    print("MEDIUM RISK")
else:
    print("HIGH RISK")

print("\nRecommendations")
print("-" * 30)

print("✓ Remove undocumented APIs")
print("✓ Update Swagger documentation")
print("✓ Secure sensitive endpoints")
print("✓ Review authentication policies")