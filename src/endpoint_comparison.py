import json


def load_documented():
    with open("datasets/swagger.json", "r") as file:
        data = json.load(file)
    return set(data["paths"].keys())


def load_active():
    with open("logs/active_endpoints.txt", "r") as file:
        return set(line.strip() for line in file if line.strip())


documented = load_documented()
active = load_active()

print("=" * 60)
print("APIHAWK ENDPOINT COMPARISON ENGINE")
print("=" * 60)

all_endpoints = sorted(documented | active)

print(f"\n{'Endpoint':<25}{'Status'}")
print("-" * 40)

for endpoint in all_endpoints:

    if endpoint in documented and endpoint in active:
        status = "✓ Documented & Active"

    elif endpoint in active:
        status = "⚠ Shadow API"

    else:
        status = "❌ Missing"

    print(f"{endpoint:<25}{status}")