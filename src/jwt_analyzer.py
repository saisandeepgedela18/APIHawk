"""
APIHawk JWT Security Analyzer
Version 1.0
"""

import base64
import json


def decode_base64url(data):
    """Decode Base64 URL safely."""

    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def analyze_jwt(token):

    findings = []

    parts = token.split(".")

    if len(parts) != 3:

        findings.append({
            "severity": "CRITICAL",
            "issue": "Invalid JWT Format",
            "recommendation": "JWT must contain Header.Payload.Signature"
        })

        return findings

    try:

        header = json.loads(
            decode_base64url(parts[0]).decode()
        )

        payload = json.loads(
            decode_base64url(parts[1]).decode()
        )

    except Exception:

        findings.append({
            "severity": "CRITICAL",
            "issue": "JWT Decoding Failed",
            "recommendation": "Malformed or corrupted JWT."
        })

        return findings

    # ---------------------------
    # Algorithm Check
    # ---------------------------

    algorithm = header.get("alg")

    if algorithm == "none":

        findings.append({
            "severity": "CRITICAL",
            "issue": "Unsigned JWT",
            "recommendation":
            "Never use alg='none' in production."
        })

    elif algorithm not in ["HS256", "RS256"]:

        findings.append({
            "severity": "MEDIUM",
            "issue": f"Unexpected Algorithm ({algorithm})",
            "recommendation":
            "Use strong signing algorithms."
        })

    # ---------------------------
    # Required Claims
    # ---------------------------

    required = ["exp", "iat", "sub"]

    for claim in required:

        if claim not in payload:

            findings.append({
                "severity": "HIGH",
                "issue": f"Missing '{claim}' Claim",
                "recommendation":
                f"Include '{claim}' in JWT payload."
            })

    return findings


if __name__ == "__main__":

    # Sample JWT (for testing only)
    sample_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ."
        "dummy_signature"
    )

    print("\n========== JWT SECURITY ANALYSIS ==========\n")

    results = analyze_jwt(sample_token)

    if results:

        for finding in results:

            print(f"Severity : {finding['severity']}")
            print(f"Issue    : {finding['issue']}")
            print(f"Fix      : {finding['recommendation']}")
            print("-" * 60)

    else:

        print("No security issues found.")