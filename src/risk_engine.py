"""
APIHawk Risk Assessment Engine
Assigns a security risk level and reason for an API endpoint.
"""


def classify_endpoint(endpoint):

    endpoint = endpoint.lower()

    # Critical Risk
    if "admin" in endpoint or "debug" in endpoint:
        return (
            "CRITICAL",
            "Administrative / Debug Endpoint"
        )

    # High Risk
    elif (
        "patient" in endpoint or
        "delete" in endpoint or
        "internal" in endpoint
    ):
        return (
            "HIGH",
            "Sensitive Healthcare or Destructive Endpoint"
        )

    # Medium Risk
    elif (
        "user" in endpoint or
        "account" in endpoint
    ):
        return (
            "MEDIUM",
            "User Management Endpoint"
        )

    # Low Risk
    elif (
        "login" in endpoint or
        "auth" in endpoint
    ):
        return (
            "LOW",
            "Authentication Endpoint"
        )

    # Default
    return (
        "LOW",
        "General API Endpoint"
    )


if __name__ == "__main__":

    samples = [
        "/admin/debug",
        "/patients",
        "/api/users",
        "/api/login",
        "/products"
    ]

    print("\n===== Risk Engine Test =====\n")

    for endpoint in samples:

        risk, reason = classify_endpoint(endpoint)

        print(f"{endpoint}")
        print(f"Risk   : {risk}")
        print(f"Reason : {reason}")
        print("-" * 40)