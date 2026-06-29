"""
APIHawk Security Service

Collects security information from all analysis modules.
"""

from database_manager import fetch_log_endpoints
from risk_engine import classify_endpoint
from owasp_engine import analyze_api


def get_security_findings():

    findings = []

    endpoints = fetch_log_endpoints()

    for method, endpoint in endpoints:

        # Risk Classification
        risk, reason = classify_endpoint(endpoint)

        # OWASP Analysis
        owasp = analyze_api(method, endpoint)

        findings.append({

            "method": method,

            "endpoint": endpoint,

            "risk": risk,

            "reason": reason,

            "owasp": owasp

        })

    return findings


if __name__ == "__main__":

    results = get_security_findings()

    print("\n===== APIHawk Security Findings =====\n")

    for item in results:

        print(f"{item['method']} {item['endpoint']}")
        print(f"Risk : {item['risk']}")
        print(f"Reason : {item['reason']}")

        if item["owasp"]:

            for finding in item["owasp"]:

                print(
                    f"OWASP : {finding['id']} - {finding['title']}"
                )

        print("-" * 50)