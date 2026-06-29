"""
APIHawk OWASP API Security Top 10 Engine
Version 1.0
"""


def analyze_api(method, endpoint):

    endpoint = endpoint.lower()

    findings = []

    # -------------------------------
    # API8 - Security Misconfiguration
    # -------------------------------
    if "debug" in endpoint or "admin" in endpoint:

        findings.append({
            "id": "API8",
            "title": "Security Misconfiguration",
            "severity": "CRITICAL",
            "recommendation":
            "Disable debug/admin endpoints in production."
        })

    # -------------------------------
    # API2 - Broken Authentication
    # -------------------------------
    if "login" in endpoint or "auth" in endpoint:

        findings.append({
            "id": "API2",
            "title": "Broken Authentication",
            "severity": "LOW",
            "recommendation":
            "Enforce MFA, secure tokens and strong authentication."
        })

    # -------------------------------
    # API1 - Broken Object Level Authorization
    # -------------------------------
    if (
        "{id}" in endpoint or
        "/users/" in endpoint or
        "/patients/" in endpoint
    ):

        findings.append({
            "id": "API1",
            "title": "Broken Object Level Authorization",
            "severity": "HIGH",
            "recommendation":
            "Validate authorization before returning object data."
        })

    # -------------------------------
    # API9 - Improper Inventory Management
    # -------------------------------
    if "test" in endpoint or "beta" in endpoint:

        findings.append({
            "id": "API9",
            "title": "Improper Inventory Management",
            "severity": "MEDIUM",
            "recommendation":
            "Remove unused or deprecated APIs."
        })

    return findings


if __name__ == "__main__":

    samples = [

        ("GET", "/admin/debug"),

        ("GET", "/api/login"),

        ("DELETE", "/users/5"),

        ("GET", "/patients/100"),

        ("GET", "/test/api")
    ]

    print("\n========== OWASP API SECURITY TEST ==========\n")

    for method, endpoint in samples:

        print(f"{method:7} {endpoint}")

        results = analyze_api(method, endpoint)

        if results:

            for item in results:

                print(f"  {item['id']}")
                print(f"  {item['title']}")
                print(f"  Severity : {item['severity']}")
                print(f"  Recommendation : {item['recommendation']}")
                print()

        else:

            print("  No OWASP Findings\n")

        print("-" * 60)