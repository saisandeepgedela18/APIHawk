import json


def load_documented_apis(swagger_file):
    """Load documented APIs from Swagger/OpenAPI file."""
    with open(swagger_file, "r") as file:
        data = json.load(file)

    return set(data["paths"].keys())


def load_active_apis(log_file):
    """Load active APIs from log file."""
    with open(log_file, "r") as file:
        return set(
            line.strip()
            for line in file
            if line.strip()
        )


def detect_shadow_apis(documented, active):
    """Find APIs running on the server but missing from documentation."""
    return active - documented


def main():
    documented = load_documented_apis("datasets/swagger.json")
    active = load_active_apis("logs/active_endpoints.txt")

    shadow = detect_shadow_apis(documented, active)

    print("=" * 55)
    print("APIHAWK ADVANCED SHADOW API DETECTOR")
    print("=" * 55)

    print(f"\nDocumented APIs : {len(documented)}")
    print(f"Active APIs     : {len(active)}")
    print(f"Shadow APIs     : {len(shadow)}")

    print("\nDocumented APIs")
    print("-" * 30)
    for api in sorted(documented):
        print(api)

    print("\nActive APIs")
    print("-" * 30)
    for api in sorted(active):
        print(api)

    print("\nShadow APIs Found")
    print("-" * 30)

    if shadow:
        for api in sorted(shadow):
            print(f"⚠ {api}")
    else:
        print("No Shadow APIs Found")


if __name__ == "__main__":
    main()