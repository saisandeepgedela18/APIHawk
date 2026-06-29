import requests

from database_manager import fetch_log_endpoints


def get_swagger_endpoints(swagger_url):
    """
    Read documented APIs from OpenAPI/Swagger.
    """

    response = requests.get(swagger_url, timeout=10)
    response.raise_for_status()

    spec = response.json()

    documented = set()

    for endpoint, methods in spec.get("paths", {}).items():

        for method in methods.keys():

            documented.add(
                (
                    method.upper(),
                    endpoint
                )
            )

    return documented


def detect_shadow_apis(swagger_url):

    # APIs extracted from Apache/Nginx logs
    logged = set(fetch_log_endpoints())

    # APIs documented in Swagger
    documented = get_swagger_endpoints(swagger_url)

    # Present in logs but not in documentation
    shadow = logged - documented

    return shadow


if __name__ == "__main__":

    swagger = "https://petstore3.swagger.io/api/v3/openapi.json"

    shadow = detect_shadow_apis(swagger)

    print("\n========== SHADOW API REPORT ==========\n")

    if shadow:

        for method, endpoint in sorted(shadow):

            print(f"{method:8} {endpoint}")

        print(f"\nTotal Shadow APIs : {len(shadow)}")

    else:

        print("No Shadow APIs Found.")