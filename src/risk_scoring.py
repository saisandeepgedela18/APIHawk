headers_found = 2
total_headers = 4

risk_score = ((total_headers - headers_found) / total_headers) * 100

print("=" * 50)
print("APIHAWK RISK SCORING ENGINE")
print("=" * 50)

print(f"Security Headers Found: {headers_found}/{total_headers}")
print(f"Risk Score: {risk_score:.0f}%")

if risk_score >= 75:
    print("Risk Level: HIGH")
elif risk_score >= 50:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")