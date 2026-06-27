import requests
from database_manager import *

# ----------------------------------------
# Initialize Database
# ----------------------------------------

create_table()
clear_old_scan()

print("=" * 60)
print("🦅 APIHAWK LIVE API SCANNER")
print("=" * 60)

# ----------------------------------------
# User Input
# ----------------------------------------

url = input("\nEnter Swagger/OpenAPI URL: ").strip()

try:

    print("\nDownloading OpenAPI Specification...\n")

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("❌ Unable to download specification.")
        print("Status Code :", response.status_code)
        exit()

    api_spec = response.json()

    print("✅ Specification Downloaded Successfully\n")

    # ----------------------------------------
    # API Information
    # ----------------------------------------

    info = api_spec.get("info", {})

    print("=" * 60)
    print("API INFORMATION")
    print("=" * 60)

    print("Title       :", info.get("title", "Unknown"))
    print("Version     :", info.get("version", "Unknown"))
    print("Description :", info.get("description", "Not Available"))

    print("\n" + "=" * 60)
    print("DISCOVERED API ENDPOINTS")
    print("=" * 60)

    paths = api_spec.get("paths", {})

    endpoint_count = 0

    sensitive_count = 0

    shadow_count = 0

    low_count = 0
        # ----------------------------------------
    # Endpoint Discovery & Risk Classification
    # ----------------------------------------

    for endpoint, methods in paths.items():

        print(f"\nEndpoint : {endpoint}")

        for method in methods.keys():

            endpoint_count += 1

            endpoint_lower = endpoint.lower()

            category = "Normal API"
            risk = "LOW"

            # Sensitive Endpoint Detection
            if any(keyword in endpoint_lower for keyword in [
                "login",
                "logout",
                "admin",
                "auth",
                "password",
                "token",
                "user"
            ]):
                category = "Sensitive Endpoint"
                risk = "HIGH"
                sensitive_count += 1

            # Shadow API Detection
            if any(keyword in endpoint_lower for keyword in [
                "debug",
                "internal",
                "test",
                "dev"
            ]):
                category = "Shadow API"
                risk = "CRITICAL"
                shadow_count += 1

            if risk == "LOW":
                low_count += 1

            # Save to SQLite
            insert_endpoint(
                endpoint,
                method.upper(),
                category,
                risk
            )

            print(
                f"{endpoint_count:2}. "
                f"{method.upper():6} | "
                f"{category:20} | "
                f"{risk}"
            )
                # ----------------------------------------
    # Scan Summary
    # ----------------------------------------

    print("\n" + "=" * 60)
    print("SCAN SUMMARY")
    print("=" * 60)

    stats = statistics()

    print(f"Total Endpoints      : {stats['total']}")
    print(f"Sensitive Endpoints  : {stats['sensitive']}")
    print(f"Shadow APIs          : {stats['shadow']}")
    print(f"Critical APIs        : {stats['critical']}")
    print(f"High Risk APIs       : {stats['high']}")
    print(f"Low Risk APIs        : {stats['low']}")

    if stats["critical"] > 0:
        overall_risk = "CRITICAL"
    elif stats["high"] > 0:
        overall_risk = "HIGH"
    else:
        overall_risk = "LOW"

    print(f"\nOverall Risk         : {overall_risk}")

    print("=" * 60)

    print("\n✅ Scan results saved to SQLite database.")

except requests.exceptions.RequestException as e:

    print("\n❌ Connection Error")
    print(e)

except Exception as e:

    print("\n❌ Error while scanning API")
    print(e)