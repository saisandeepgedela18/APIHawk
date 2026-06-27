import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard_data import get_dashboard_data
# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="APIHawk Security Dashboard",
    page_icon="🦅",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------
dashboard = get_dashboard_data()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🦅 APIHawk")

st.sidebar.markdown("---")

st.sidebar.success("Project Status")

st.sidebar.write("✅ API Discovery")
st.sidebar.write("✅ Shadow API Detection")
st.sidebar.write("✅ Sensitive Endpoint Detection")
st.sidebar.write("✅ SQLite Database")
st.sidebar.write("✅ HTML Report")
st.sidebar.write("✅ PDF Report")
st.sidebar.write("✅ Analytics Dashboard")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### APIHawk v1.0

Professional API Security Assessment Framework

Features

• API Discovery

• Swagger Analysis

• Shadow API Detection

• Authentication Detection

• Risk Classification

• SQLite Database

• HTML Reports

• PDF Reports

• Analytics Dashboard
"""
)

# ----------------------------
# Header
# ----------------------------

st.title("🦅 APIHawk Security Dashboard")

st.caption("Professional API Security Assessment & Monitoring Platform")

st.markdown("---")

# ----------------------------
# Dashboard Metrics
# ----------------------------

col1,col2,col3,col4=st.columns(4)

col1.metric(
"Total APIs",
dashboard["total_apis"]
)

col2.metric(
"Shadow APIs",
dashboard["shadow_apis"]
)

col3.metric(
"Sensitive APIs",
dashboard["sensitive_apis"]
)

col4.metric(
"Overall Risk",
dashboard["risk"]
)

st.markdown("---")

# ----------------------------
# Security Summary
# ----------------------------

left,right=st.columns([2,1])

with left:

    st.subheader("Security Summary")

    st.success("✔ Swagger Documentation Loaded")

    st.success("✔ Authentication Detected")

    st.warning("⚠ Shadow APIs Found")

    st.warning("⚠ Sensitive APIs Found")

with right:

    st.subheader("Overall Security Score")

    if dashboard["risk"]=="CRITICAL":
        score=40

    elif dashboard["risk"]=="HIGH":
        score=70

    elif dashboard["risk"]=="MEDIUM":
        score=85

    else:
        score=95

    st.progress(score)

    st.error(dashboard["risk"])

    st.caption(f"Security Score : {score}/100")

st.markdown("---")
# ----------------------------
# Charts
# ----------------------------

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader("📊 Risk Distribution")

    fig, ax = plt.subplots(figsize=(5,5))

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

    st.subheader("📈 API Categories")

    fig2, ax2 = plt.subplots(figsize=(6,5))

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

    ax2.set_title("API Category Statistics")

    st.pyplot(fig2)

st.markdown("---")

# ----------------------------
# Recent Scan Results
# ----------------------------

st.subheader("📋 Recent Scan Results")

scan_data = {
    "Endpoint": [
        "/login",
        "/admin/debug",
        "/patients",
        "/users",
        "/appointments"
    ],

    "Method": [
        "POST",
        "GET",
        "GET",
        "GET",
        "POST"
    ],

    "Category": [
        "Sensitive Endpoint",
        "Shadow API",
        "Normal API",
        "Normal API",
        "Normal API"
    ],

    "Risk": [
        "HIGH",
        "CRITICAL",
        "LOW",
        "LOW",
        "LOW"
    ],

    "Status": [
        "⚠ Review Required",
        "🚨 Immediate Action",
        "✅ Secure",
        "✅ Secure",
        "✅ Secure"
    ]
}

df = pd.DataFrame(scan_data)

st.dataframe(df, use_container_width=True)

st.markdown("---")
# ----------------------------
# Security Recommendations
# ----------------------------

st.subheader("🛡️ Security Recommendations")

recommendations = [
    "Remove undocumented Shadow APIs immediately.",
    "Protect sensitive endpoints using strong authentication.",
    "Enable API rate limiting.",
    "Implement API request logging and monitoring.",
    "Review authentication and authorization policies.",
    "Keep Swagger/OpenAPI documentation synchronized.",
    "Perform regular API vulnerability assessments.",
    "Review exposed debug and admin endpoints."
]

for rec in recommendations:
    st.success("✔ " + rec)

st.markdown("---")

# ----------------------------
# Risk Summary
# ----------------------------

st.subheader("📌 Risk Summary")

summary = pd.DataFrame({
    "Severity": ["Critical", "High", "Medium", "Low"],
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
# Scan Information
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    st.info("""
### Scan Information

**Project:** Digital Health Gateway

**Scanner:** APIHawk v1.0

**Database:** SQLite

**Report Formats:**
- HTML
- PDF
- Dashboard
""")

with col2:
    st.info(f"""
### Current Assessment

**Overall Risk:** {dashboard["risk"]}

**Total APIs:** {dashboard["total_apis"]}

**Shadow APIs:** {dashboard["shadow_apis"]}

**Sensitive APIs:** {dashboard["sensitive_apis"]}
""")

st.markdown("---")

# ----------------------------
# Footer
# ----------------------------

st.caption(
    "🦅 APIHawk v1.0 | Professional API Security Assessment Framework"
)

st.caption(
    "Developed by Sai Sandeep Gedela | Python • Streamlit • SQLite"
)