import requests

def check_api(url):
    try:
        response = requests.get(url, timeout=5)

        print("=" * 40)
        print("API Discovery Result")
        print("=" * 40)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_api("https://jsonplaceholder.typicode.com/posts")