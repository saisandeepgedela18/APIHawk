import os
from datetime import datetime
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from dashboard.dashboard_data import get_dashboard_data
from security_service import get_security_findings

dashboard = get_dashboard_data()
findings = get_security_findings()

report_time = datetime.now().strftime("%d %B %Y %I:%M %p")

html = []

html.append("""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>APIHawk Security Report</title>

<style>

body{
font-family:Segoe UI,Arial,sans-serif;
background:#eef2f7;
margin:0;
padding:30px;
color:#333;
}

.container{
width:90%;
margin:auto;
}

.header{
background:#0f4c81;
color:white;
padding:30px;
border-radius:10px;
}

.cards{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:20px;
margin-top:20px;
}

.card{
background:white;
padding:20px;
text-align:center;
border-radius:10px;
box-shadow:0 3px 10px rgba(0,0,0,.15);
}

.section{
background:white;
margin-top:25px;
padding:20px;
border-radius:10px;
box-shadow:0 3px 10px rgba(0,0,0,.15);
}

table{
width:100%;
border-collapse:collapse;
margin-top:15px;
}

th{
background:#0f4c81;
color:white;
padding:10px;
}

td{
padding:10px;
border:1px solid #ddd;
}

.low{
background:#28a745;
color:white;
padding:5px 10px;
border-radius:20px;
}

.medium{
background:#ffc107;
padding:5px 10px;
border-radius:20px;
}

.high{
background:#ff9800;
color:white;
padding:5px 10px;
border-radius:20px;
}

.critical{
background:#dc3545;
color:white;
padding:5px 10px;
border-radius:20px;
}

.footer{
margin-top:40px;
text-align:center;
color:#666;
}

</style>

</head>

<body>

<div class="container">
""")

html.append(f"""

<div class="header">

<h1>🦅 APIHawk Security Assessment Report</h1>

<p><b>Generated:</b> {report_time}</p>

<p><b>Project:</b> Digital Health Gateway</p>

<p><b>Framework:</b> APIHawk v2.0</p>

</div>

<div class="cards">

<div class="card">

<h3>Total APIs</h3>

<h1>{dashboard["total_apis"]}</h1>

</div>

<div class="card">

<h3>Shadow APIs</h3>

<h1>{dashboard["shadow_apis"]}</h1>

</div>

<div class="card">

<h3>Sensitive APIs</h3>

<h1>{dashboard["sensitive_apis"]}</h1>

</div>

<div class="card">

<h3>Security Score</h3>

<h1>{dashboard["security_score"]}%</h1>

</div>

</div>

<div class="section">

<h2>Executive Summary</h2>

<p>

APIHawk performed an automated API Security Assessment using Shadow API Discovery,
Risk Classification, OWASP API Security checks and JWT Authentication Review.

</p>

<p>

<b>Overall Risk:</b> {dashboard["risk"]}

</p>

</div>

""")
# -----------------------------------------
# Security Statistics
# -----------------------------------------

html.append(f"""

<div class="section">

<h2>📊 Security Statistics</h2>

<table>

<tr>

<th>Metric</th>

<th>Value</th>

</tr>

<tr>

<td>Total APIs</td>

<td>{dashboard["total_apis"]}</td>

</tr>

<tr>

<td>Shadow APIs</td>

<td>{dashboard["shadow_apis"]}</td>

</tr>

<tr>

<td>Sensitive APIs</td>

<td>{dashboard["sensitive_apis"]}</td>

</tr>

<tr>

<td>OWASP Findings</td>

<td>{dashboard["owasp_findings"]}</td>

</tr>

<tr>

<td>JWT Issues</td>

<td>{dashboard["jwt_issues"]}</td>

</tr>

<tr>

<td>Overall Risk</td>

<td>{dashboard["risk"]}</td>

</tr>

</table>

</div>

""")

# -----------------------------------------
# Security Findings
# -----------------------------------------

rows = ""

for item in findings:

    badge = "low"

    if item["risk"] == "CRITICAL":
        badge = "critical"

    elif item["risk"] == "HIGH":
        badge = "high"

    elif item["risk"] == "MEDIUM":
        badge = "medium"

    rows += f"""
<tr>

<td>{item['method']}</td>

<td>{item['endpoint']}</td>

<td><span class="{badge}">{item['risk']}</span></td>

<td>{item['reason']}</td>

</tr>
"""

html.append(f"""

<div class="section">

<h2>🚨 Security Findings</h2>

<table>

<tr>

<th>Method</th>

<th>Endpoint</th>

<th>Risk</th>

<th>Reason</th>

</tr>

{rows}

</table>

</div>

""")

# -----------------------------------------
# Risk Distribution
# -----------------------------------------

html.append(f"""

<div class="section">

<h2>📈 Risk Distribution</h2>

<table>

<tr>

<th>Severity</th>

<th>Count</th>

</tr>

<tr>

<td>Critical</td>

<td>{dashboard["critical"]}</td>

</tr>

<tr>

<td>High</td>

<td>{dashboard["high"]}</td>

</tr>

<tr>

<td>Medium</td>

<td>{dashboard["medium"]}</td>

</tr>

<tr>

<td>Low</td>

<td>{dashboard["low"]}</td>

</tr>

</table>

</div>

""")
# -----------------------------------------
# OWASP Summary
# -----------------------------------------

html.append(f"""

<div class="section">

<h2>🛡️ OWASP API Security Summary</h2>

<table>

<tr>
<th>Check</th>
<th>Status</th>
</tr>

<tr>
<td>Shadow API Discovery</td>
<td>Completed</td>
</tr>

<tr>
<td>Risk Classification</td>
<td>Completed</td>
</tr>

<tr>
<td>OWASP Findings</td>
<td>{dashboard["owasp_findings"]}</td>
</tr>

<tr>
<td>JWT Authentication Issues</td>
<td>{dashboard["jwt_issues"]}</td>
</tr>

<tr>
<td>Overall Risk</td>
<td>{dashboard["risk"]}</td>
</tr>

<tr>
<td>Security Score</td>
<td>{dashboard["security_score"]}%</td>
</tr>

</table>

</div>

""")

# -----------------------------------------
# Recommendations
# -----------------------------------------

html.append("""

<div class="section">

<h2>💡 Security Recommendations</h2>

<ul>

<li>Remove undocumented Shadow APIs.</li>

<li>Protect sensitive endpoints using strong authentication.</li>

<li>Enable API rate limiting.</li>

<li>Enable API monitoring and centralized logging.</li>

<li>Review OWASP API Security Top 10 regularly.</li>

<li>Rotate JWT signing keys periodically.</li>

<li>Keep Swagger/OpenAPI documentation updated.</li>

<li>Disable debug and admin endpoints in production.</li>

</ul>

</div>

""")

# -----------------------------------------
# Footer
# -----------------------------------------

html.append(f"""

<div class="footer">

<hr>

<h2>APIHawk v2.0</h2>

<p>

Professional API Security Assessment Framework

</p>

<p>

Generated : {report_time}

</p>

<p>

Developed by Sai Sandeep Gedela

</p>

</div>

</div>

</body>

</html>

""")

# -----------------------------------------
# Save Report
# -----------------------------------------

os.makedirs("reports", exist_ok=True)

report_path = "reports/security_report.html"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("".join(html))

print("=" * 70)
print("APIHAWK HTML REPORT GENERATOR")
print("=" * 70)
print("HTML Report Generated Successfully")
print(f"Report : {report_path}")
print(f"Generated : {report_time}")
print(f"Security Score : {dashboard['security_score']}%")
print(f"Overall Risk : {dashboard['risk']}")
print("=" * 70)
