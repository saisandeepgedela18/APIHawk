import json

with open("datasets/swagger.json", "r") as file:
    data = json.load(file)

print("=" * 50)
print("APIHAWK AUTHENTICATION DETECTOR")
print("=" * 50)

security = data.get("security", [])
schemes = data.get("components", {}).get("securitySchemes", {})

if not security:
    print("\nNo Authentication Detected")
else:
    print("\nAuthentication Methods Found:\n")

    for scheme_name in schemes:
        scheme = schemes[scheme_name]

        auth_type = scheme.get("type", "Unknown")
        auth_scheme = scheme.get("scheme", "")

        print(f"Name   : {scheme_name}")
        print(f"Type   : {auth_type}")
        print(f"Scheme : {auth_scheme}")
        print("-" * 40)