import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# -----------------------------
# Import Project Modules
# -----------------------------

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from dashboard_data import get_dashboard_data
from security_service import get_security_findings

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="APIHawk Security Dashboard",
    page_icon="🦅",
    layout="wide"
)

# -----------------------------
# Load Dashboard Data
# -----------------------------

dashboard = get_dashboard_data()

# -----------------------------
# Calculate Security Score
# -----------------------------

security_score = 100

security_score -= dashboard["critical"] * 25
security_score -= dashboard["high"] * 8
security_score -= dashboard["medium"] * 4
security_score -= dashboard["low"] * 1

security_score = max(security_score, 0)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🦅 APIHawk")

st.sidebar.markdown("---")

st.sidebar.success("Project Status")

st.sidebar.write("✅ API Discovery")
st.sidebar.write("✅ Shadow API Detection")
st.sidebar.write("✅ Risk Classification")
st.sidebar.write("✅ OWASP Analysis")
st.sidebar.write("✅ JWT Analyzer")
st.sidebar.write("✅ SQLite Database")
st.sidebar.write("✅ HTML Reports")
st.sidebar.write("✅ PDF Reports")
st.sidebar.write("✅ Dashboard")

st.sidebar.markdown("---")

st.sidebar.info("""
### APIHawk v2.0

Professional API Security Assessment Framework

**Modules**

• API Discovery

• Swagger Analysis

• Shadow API Detection

• OWASP API Security

• JWT Analyzer

• Risk Classification

• SQLite Database

• HTML Reports

• PDF Reports

• Analytics Dashboard
""")

# -----------------------------
# Header
# -----------------------------

st.title("🦅 APIHawk Security Dashboard")

st.caption(
    "Professional API Security Assessment & Monitoring Platform"
)

st.markdown("---")

# -----------------------------
# Top Metrics
# -----------------------------

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "Total APIs",
        dashboard["total_apis"]
    )

with m2:
    st.metric(
        "Shadow APIs",
        dashboard["shadow_apis"]
    )

with m3:
    st.metric(
        "Sensitive APIs",
        dashboard["sensitive_apis"]
    )

with m4:
    st.metric(
        "Overall Risk",
        dashboard["risk"]
    )

st.divider()

# -----------------------------
# Security Center
# -----------------------------

st.header("🛡️ Security Center")

sec1, sec2, sec3, sec4 = st.columns(4)

with sec1:
    st.metric(
        "Shadow APIs",
        dashboard["shadow_apis"]
    )

with sec2:
    st.metric(
        "OWASP Findings",
        dashboard["owasp_findings"]
    )

with sec3:
    st.metric(
        "JWT Issues",
        dashboard["jwt_issues"]
    )

with sec4:
    st.metric(
        "Security Score",
        f"{security_score}%"
    )

st.markdown("---")

# -----------------------------
# Latest Security Findings
# -----------------------------

st.subheader("🚨 Latest Security Findings")

findings = get_security_findings()

rows = []

for item in findings:

    rows.append({

        "Method": item["method"],

        "Endpoint": item["endpoint"],

        "Risk": item["risk"],

        "Reason": item["reason"]

    })

findings_df = pd.DataFrame(rows)

st.dataframe(
    findings_df,
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# Security Summary
# -----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("Security Summary")

    st.success("✔ Swagger Documentation Loaded")

    st.success("✔ Authentication Detected")

    if dashboard["shadow_apis"] > 0:
        st.warning(
            f"⚠ {dashboard['shadow_apis']} Shadow APIs Found"
        )
    else:
        st.success("✔ No Shadow APIs Found")

    if dashboard["sensitive_apis"] > 0:
        st.warning(
            f"⚠ {dashboard['sensitive_apis']} Sensitive APIs Found"
        )
    else:
        st.success("✔ No Sensitive APIs Found")

    if dashboard["critical"] > 0:
        st.error(
            f"🚨 Critical APIs : {dashboard['critical']}"
        )

    if dashboard["high"] > 0:
        st.warning(
            f"⚠ High Risk APIs : {dashboard['high']}"
        )

    if dashboard["medium"] > 0:
        st.info(
            f"ℹ Medium Risk APIs : {dashboard['medium']}"
        )

    if dashboard["low"] > 0:
        st.success(
            f"✔ Low Risk APIs : {dashboard['low']}"
        )

with right:

    st.subheader("Overall Security Score")

    st.progress(security_score)

    st.error(dashboard["risk"])

    st.caption(
        f"Security Score : {security_score}/100"
    )

st.markdown("---")
# ----------------------------
# Charts
# ----------------------------

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader("📊 Risk Distribution")

    fig, ax = plt.subplots(figsize=(5, 5))

    labels = [
        "Critical",
        "High",
        "Medium",
        "Low"
    ]

    values = [
        dashboard["critical"],
        dashboard["high"],
        dashboard["medium"],
        dashboard["low"]
    ]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

with chart2:

    st.subheader("📈 API Statistics")

    fig2, ax2 = plt.subplots(figsize=(6, 5))

    categories = [
        "Total APIs",
        "Shadow APIs",
        "Sensitive APIs"
    ]

    counts = [
        dashboard["total_apis"],
        dashboard["shadow_apis"],
        dashboard["sensitive_apis"]
    ]

    ax2.bar(categories, counts)

    ax2.set_ylabel("Count")
    ax2.set_title("API Statistics")

    st.pyplot(fig2)

st.markdown("---")

# ----------------------------
# Risk Summary
# ----------------------------

st.subheader("📌 Risk Summary")

summary = pd.DataFrame({

    "Severity": [
        "Critical",
        "High",
        "Medium",
        "Low"
    ],

    "Count": [

        dashboard["critical"],
        dashboard["high"],
        dashboard["medium"],
        dashboard["low"]

    ]

})

st.table(summary)

st.markdown("---")

# ----------------------------
# Security Recommendations
# ----------------------------

st.subheader("🛡️ Security Recommendations")

recommendations = [

    "Remove undocumented Shadow APIs immediately.",

    "Protect sensitive endpoints using authentication and authorization.",

    "Implement API rate limiting.",

    "Enable API request logging and monitoring.",

    "Review OWASP API Security Top 10 controls.",

    "Keep Swagger/OpenAPI documentation synchronized.",

    "Rotate JWT signing secrets regularly.",

    "Disable debug and admin endpoints in production."

]

for rec in recommendations:

    st.success("✔ " + rec)

st.markdown("---")

# ----------------------------
# Project Information
# ----------------------------

left, right = st.columns(2)

with left:

    st.info(f"""
### Project Information

**Project**

APIHawk

**Version**

2.0

**Framework**

Python + Streamlit

**Database**

SQLite

**Reports**

• HTML

• PDF
""")

with right:

    st.info(f"""
### Current Scan

**Overall Risk**

{dashboard["risk"]}

**Security Score**

{security_score}/100

**OWASP Findings**

{dashboard["owasp_findings"]}

**JWT Issues**

{dashboard["jwt_issues"]}
""")

st.markdown("---")

# ----------------------------
# Scan Results
# ----------------------------

st.subheader("📋 Live Scan Results")

scan_rows = []

for item in findings:

    status = "✅ Secure"

    if item["risk"] == "CRITICAL":
        status = "🚨 Critical"

    elif item["risk"] == "HIGH":
        status = "⚠ High"

    elif item["risk"] == "MEDIUM":
        status = "🟡 Medium"

    scan_rows.append({

        "Method": item["method"],
        "Endpoint": item["endpoint"],
        "Risk": item["risk"],
        "Status": status

    })

scan_df = pd.DataFrame(scan_rows)

st.dataframe(
    scan_df,
    use_container_width=True
)

st.markdown("---")

# ----------------------------
# Footer
# ----------------------------

st.caption(
    "🦅 APIHawk v2.0 | Professional API Security Assessment Framework"
)

st.caption(
    "Developed by Sai Sandeep Gedela"
)

st.caption(
    "Python • Streamlit • SQLite • OWASP API Security • JWT Analysis"
)