import os
from datetime import datetime

report_time = datetime.now().strftime("%d %B %Y %I:%M %p")

html = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>APIHawk Security Report</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:Arial,Helvetica,sans-serif;
    background:#edf2f7;
    color:#333;
}

.container{
    width:90%;
    margin:30px auto;
}

.header{
    background:#0f4c81;
    color:white;
    padding:30px;
    border-radius:12px;
    box-shadow:0 5px 15px rgba(0,0,0,.15);
}

.header h1{
    font-size:34px;
}

.header p{
    margin-top:8px;
}

.cards{
    display:flex;
    gap:20px;
    margin-top:25px;
}

.card{
    flex:1;
    background:white;
    padding:
        border-radius:10px;
    text-align:center;
    box-shadow:0 3px 10px rgba(0,0,0,.15);
}

.card h3{
    color:#0f4c81;
    margin-bottom:10px;
}

.card p{
    font-size:30px;
    font-weight:bold;
}

.summary{
    margin-top:30px;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,.15);
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th{
    background:#0f4c81;
    color:white;
    padding:12px;
}

td{
    padding:12px;
    border:1px solid #ddd;
}

.badge-low{
    background:#28a745;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-weight:bold;
}

.badge-high{
    background:#ff9800;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-weight:bold;
}

.badge-critical{
    background:#dc3545;
    color:white;
    padding:6px 12px;
    border-radius:20px;
    font-weight:bold;
}

.recommendations{
    margin-top:30px;
    background:white;
    padding:20px;
    border-left:8px solid #0f4c81;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,.15);
}

.footer{
    margin-top:40px;
    text-align:center;
    color:#666;
    padding:20px;
}

</style>

</head>

<body>

<div class="container">

<div class="header">

<h1>🦅 APIHawk Security Assessment Report</h1>

<p><b>Project:</b> Digital Health Gateway</p>

<p><b>Scan ID:</b> API-2026-001</p>

<p><b>Generated:</b> {REPORT_TIME}</p>

<p><b>Version:</b> APIHawk v1.0</p>

</div>

<div class="cards">

<div class="card">
<h3>Total APIs</h3>
<p>6</p>
</div>

<div class="card">
<h3>Shadow APIs</h3>
<p>2</p>
</div>

<div class="card">
<h3>Sensitive APIs</h3>
<p>2</p>
</div>

<div class="card">
<h3>Risk Level</h3>
<p style="color:red;">HIGH</p>
</div>

</div>
<div class="summary">

<h2>📋 Executive Summary</h2>

<br>

<p>

APIHawk analyzed the OpenAPI/Swagger specification and evaluated
all available API endpoints.

The assessment identified undocumented Shadow APIs,
Sensitive Endpoints and potential API security risks.

Based on the findings, the application currently has an
<b style="color:#dc3545;">HIGH RISK</b> security posture that
requires immediate review.

</p>

</div>

<div class="summary">

<h2>📈 Overall Security Score</h2>

<br>

<progress value="70" max="100"
style="width:100%;height:28px;">
</progress>

<br><br>

<h3 style="color:#dc3545;">
70 / 100 (HIGH RISK)
</h3>

</div>

<div class="summary">

<h2>📊 Scan Statistics</h2>

<br>

<table>

<tr>
<th>Parameter</th>
<th>Value</th>
</tr>

<tr>
<td>Total APIs Scanned</td>
<td>6</td>
</tr>

<tr>
<td>Shadow APIs</td>
<td>2</td>
</tr>

<tr>
<td>Sensitive APIs</td>
<td>2</td>
</tr>

<tr>
<td>Authentication</td>
<td>Bearer Token</td>
</tr>

<tr>
<td>Swagger Documentation</td>
<td>Available</td>
</tr>

<tr>
<td>Overall Risk</td>
<td><span class="badge-high">HIGH</span></td>
</tr>

</table>

</div>

<div class="summary">

<h2>📄 Detected Endpoints</h2>

<br>

<table>

<tr>

<th>Endpoint</th>
<th>Method</th>
<th>Category</th>
<th>Risk</th>
<th>Status</th>

</tr>

<tr>

<td>/login</td>
<td>POST</td>
<td>Sensitive Endpoint</td>
<td><span class="badge-high">HIGH</span></td>
<td>⚠ Review Required</td>

</tr>

<tr>

<td>/admin/debug</td>
<td>GET</td>
<td>Shadow API</td>
<td><span class="badge-critical">CRITICAL</span></td>
<td>🚨 Immediate Action</td>

</tr>

<tr>

<td>/patients</td>
<td>GET</td>
<td>Normal API</td>
<td><span class="badge-low">LOW</span></td>
<td>✅ Secure</td>

</tr>

<tr>

<td>/users</td>
<td>GET</td>
<td>Normal API</td>
<td><span class="badge-low">LOW</span></td>
<td>✅ Secure</td>

</tr>

<tr>

<td>/appointments</td>
<td>POST</td>
<td>Normal API</td>
<td><span class="badge-low">LOW</span></td>
<td>✅ Secure</td>

</tr>

</table>

</div>
<div class="summary">

<h2>🚨 Risk Breakdown</h2>

<br>

<table>

<tr>
<th>Severity</th>
<th>Count</th>
</tr>

<tr>
<td>🔴 Critical</td>
<td>1</td>
</tr>

<tr>
<td>🟠 High</td>
<td>1</td>
</tr>

<tr>
<td>🟡 Medium</td>
<td>0</td>
</tr>

<tr>
<td>🟢 Low</td>
<td>4</td>
</tr>

</table>

</div>

<div class="summary">

<h2>🛡️ Security Status</h2>

<br>

<table>

<tr>
<th>Module</th>
<th>Status</th>
</tr>

<tr>
<td>Swagger Documentation</td>
<td>✅ PASS</td>
</tr>

<tr>
<td>Authentication Detection</td>
<td>✅ PASS</td>
</tr>

<tr>
<td>Shadow API Detection</td>
<td>⚠ FOUND</td>
</tr>

<tr>
<td>Sensitive Endpoint Detection</td>
<td>⚠ FOUND</td>
</tr>

<tr>
<td>Overall Assessment</td>
<td><span class="badge-high">HIGH RISK</span></td>
</tr>

</table>

</div>

<div class="recommendations">

<h2>💡 Security Recommendations</h2>

<br>

<ul>

<li>✔ Remove undocumented Shadow APIs.</li>
<li>✔ Protect sensitive endpoints.</li>
<li>✔ Enable API rate limiting.</li>
<li>✔ Enable API monitoring and logging.</li>
<li>✔ Keep Swagger documentation synchronized.</li>
<li>✔ Perform regular API security assessments.</li>

</ul>

</div>

<div class="footer">

<hr>

<h3>🦅 APIHawk v1.0</h3>

<p><b>Shadow API Discovery & Vulnerability Assessment Framework</b></p>

<p>Developed by <b>Sai Sandeep Gedela</b></p>

<p>Generated on: {REPORT_TIME}</p>

<p>© 2026 APIHawk. All Rights Reserved.</p>

</div>

</div>

</body>

</html>
"""

html = html.replace("{REPORT_TIME}", report_time)

os.makedirs("reports", exist_ok=True)

with open("reports/security_report.html", "w", encoding="utf-8") as file:
    file.write(html)

print("=" * 60)
print("🦅 APIHAWK HTML REPORT GENERATOR")
print("=" * 60)
print("✅ HTML Report Generated Successfully")
print(f"📅 Generated : {report_time}")
print("📁 Saved to : reports/security_report.html")
