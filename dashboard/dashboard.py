import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="APIHawk Security Dashboard",
    page_icon="🦅",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🦅 APIHawk")
st.sidebar.markdown("---")

st.sidebar.success("Project Status")
st.sidebar.write("✅ Core Modules Completed")
st.sidebar.write("✅ Database Integrated")
st.sidebar.write("✅ Dashboard Active")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **APIHawk v1.0**

    API Security Assessment Tool

    Features:
    - Shadow API Detection
    - Sensitive Endpoint Detection
    - Risk Classification
    - Security Reports
    """
)

# -----------------------------
# Header
# -----------------------------
st.title("🦅 APIHawk Security Dashboard")
st.markdown("### API Security Assessment & Monitoring")
st.markdown("---")

# -----------------------------
# Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total APIs", "6")
col2.metric("Shadow APIs", "2", delta="+2")
col3.metric("Sensitive APIs", "2")
col4.metric("Risk Level", "HIGH")

st.markdown("---")

# -----------------------------
# Security Status
# -----------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("Security Summary")

    st.success("✔ Swagger Documentation Loaded")
    st.success("✔ Authentication Detected")
    st.warning("⚠ Shadow APIs Detected")
    st.warning("⚠ Sensitive Endpoints Identified")

with right:
    st.subheader("Overall Risk")

    st.error("🔴 HIGH")

    st.progress(70)

    st.caption("Security Score: 70/100")

st.markdown("---")

# -----------------------------
# Scan Results
# -----------------------------
st.subheader("Recent Scan Results")

data = {
    "Endpoint": [
        "/login",
        "/admin/debug",
        "/patients",
        "/users",
        "/appointments"
    ],
    "Category": [
        "Sensitive",
        "Shadow API",
        "Normal",
        "Normal",
        "Normal"
    ],
    "Risk": [
        "HIGH",
        "CRITICAL",
        "LOW",
        "LOW",
        "LOW"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.markdown("---")

# -----------------------------
# Recommendations
# -----------------------------
st.subheader("Security Recommendations")

st.write("✅ Remove undocumented APIs")
st.write("✅ Secure sensitive endpoints")
st.write("✅ Review authentication policies")
st.write("✅ Update Swagger documentation")
st.write("✅ Perform regular API security scans")

st.markdown("---")

# -----------------------------
# Footer
# -----------------------------
st.caption("APIHawk v1.0 | Built using Python, Streamlit & SQLite")