import requests

url = "https://jsonplaceholder.typicode.com"

print("=" * 50)
print("APIHAWK SECURITY HEADER ANALYZER")
print("=" * 50)

try:
    response = requests.get(url)

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    for header in security_headers:
        if header in response.headers:
            print(f"{header} --> PRESENT")
        else:
            print(f"{header} --> MISSING")

except Exception as e:
    print("Error:", e)