import json

SENSITIVE_KEYWORDS = [
    "admin",
    "login",
    "password",
    "token",
    "auth",
    "config",
    "debug",
    "reset",
    "user"
]

with open("datasets/swagger.json", "r") as file:
    swagger = json.load(file)

documented = set(swagger["paths"].keys())

with open("logs/active_endpoints.txt", "r") as file:
    active = set(line.strip() for line in file if line.strip())

shadow = active - documented

sensitive = []

for endpoint in documented:
    endpoint_lower = endpoint.lower()

    for keyword in SENSITIVE_KEYWORDS:
        if keyword in endpoint_lower:
            sensitive.append(endpoint)
            break

score = 0

score += len(shadow) * 25
score += len(sensitive) * 10

if score >= 80:
    risk = "CRITICAL"

elif score >= 50:
    risk = "HIGH"

elif score >= 25:
    risk = "MEDIUM"

else:
    risk = "LOW"

print("=" * 60)
print("APIHAWK RISK CLASSIFICATION ENGINE")
print("=" * 60)

print(f"Shadow APIs        : {len(shadow)}")
print(f"Sensitive APIs     : {len(sensitive)}")
print(f"Risk Score         : {score}/100")
print(f"Overall Risk Level : {risk}")