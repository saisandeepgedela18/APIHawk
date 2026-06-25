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


def load_endpoints():
    with open("datasets/swagger.json", "r") as file:
        data = json.load(file)

    return data["paths"].keys()


def detect_sensitive(endpoints):
    sensitive = []

    for endpoint in endpoints:
        endpoint_lower = endpoint.lower()

        for keyword in SENSITIVE_KEYWORDS:
            if keyword in endpoint_lower:
                sensitive.append((endpoint, keyword))
                break

    return sensitive


def main():

    endpoints = load_endpoints()
    sensitive = detect_sensitive(endpoints)

    print("=" * 60)
    print("APIHAWK SENSITIVE ENDPOINT DETECTOR")
    print("=" * 60)

    print(f"\nTotal APIs Checked : {len(list(endpoints))}")
    print(f"Sensitive APIs     : {len(sensitive)}")

    print("\nSensitive Endpoints")
    print("-" * 35)

    if sensitive:
        for endpoint, keyword in sensitive:
            print(f"⚠ {endpoint}   (Matched: {keyword})")
    else:
        print("No Sensitive Endpoints Found")


if __name__ == "__main__":
    main()