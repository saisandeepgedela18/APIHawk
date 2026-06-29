import requests

from database_manager import fetch_log_endpoints
from risk_engine import classify_endpoint


def get_swagger_endpoints(swagger_url):
    """Read documented APIs from OpenAPI/Swagger."""

    response = requests.get(swagger_url, timeout=10)
    response.raise_for_status()

    spec = response.json()

    documented = set()

    for endpoint, methods in spec.get("paths", {}).items():
        for method in methods.keys():
            documented.add((method.upper(), endpoint))

    return documented


def detect_shadow_apis(swagger_url):

    logged = set(fetch_log_endpoints())

    documented = get_swagger_endpoints(swagger_url)

    shadow = logged - documented

    return shadow


if __name__ == "__main__":

    swagger = "https://petstore3.swagger.io/api/v3/openapi.json"

    shadow = detect_shadow_apis(swagger)

    print("\n========== SHADOW API SECURITY REPORT ==========\n")

    if shadow:

        critical = 0
        high = 0
        medium = 0
        low = 0

        for method, endpoint in sorted(shadow):

            risk, reason = classify_endpoint(endpoint)

            print(f"{method:8} {endpoint}")
            print(f"Risk   : {risk}")
            print(f"Reason : {reason}")
            print("-" * 50)

            if risk == "CRITICAL":
                critical += 1
            elif risk == "HIGH":
                high += 1
            elif risk == "MEDIUM":
                medium += 1
            else:
                low += 1

        print("\n========== SUMMARY ==========\n")

        print(f"Critical APIs : {critical}")
        print(f"High APIs     : {high}")
        print(f"Medium APIs   : {medium}")
        print(f"Low APIs      : {low}")

        print(f"\nTotal Shadow APIs : {len(shadow)}")

    else:

        print("No Shadow APIs Found.")