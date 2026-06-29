import re
from database_manager import (
    create_log_table,
    insert_log_endpoint,
    fetch_log_endpoints
)


def parse_log(log_file):

    endpoints = []

    # Apache / Nginx Common Log Pattern
    pattern = r'"(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+([^\s]+)'

    with open(log_file, "r") as file:

        for line in file:

            match = re.search(pattern, line)

            if match:

                method = match.group(1)
                endpoint = match.group(2)

                # Remove query parameters
                endpoint = endpoint.split("?")[0]

                endpoints.append((method, endpoint))

    # Remove duplicates
    endpoints = list(set(endpoints))

    return sorted(endpoints)


if __name__ == "__main__":

    log_path = "logs/access.log"

    # Create database table
    create_log_table()

    results = parse_log(log_path)

    print("\n===== Extracted API Endpoints =====\n")

    for method, endpoint in results:

        print(f"{method:8} {endpoint}")

        # Store in SQLite
        insert_log_endpoint(method, endpoint)

    print(f"\nTotal APIs Found: {len(results)}")

    print("\n===== Stored Endpoints =====\n")

    for method, endpoint in fetch_log_endpoints():

        print(f"{method:8} {endpoint}")