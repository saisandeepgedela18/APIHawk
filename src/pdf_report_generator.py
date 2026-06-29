import os
import sys
from datetime import datetime

# -------------------------------------------------
# Project Path
# -------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# ReportLab
# -------------------------------------------------

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

# -------------------------------------------------
# APIHawk Modules
# -------------------------------------------------

from dashboard.dashboard_data import get_dashboard_data
from security_service import get_security_findings

dashboard = get_dashboard_data()
findings = get_security_findings()

report_time = datetime.now().strftime("%d %B %Y %I:%M %p")

# -------------------------------------------------
# Create Reports Folder
# -------------------------------------------------

os.makedirs("reports", exist_ok=True)

report_path = "reports/security_report.pdf"

doc = SimpleDocTemplate(
    report_path,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

elements = []

# -------------------------------------------------
# Cover Page
# -------------------------------------------------

title = Paragraph(
    "<font size='24' color='darkblue'><b>APIHawk Security Assessment Report</b></font>",
    styles["Title"]
)

elements.append(title)

elements.append(Spacer(1, 20))

elements.append(
    Paragraph(
        f"<b>Project :</b> Digital Health Gateway",
        styles["Normal"]
    )
)

elements.append(
    Paragraph(
        f"<b>Framework :</b> APIHawk v2.0",
        styles["Normal"]
    )
)

elements.append(
    Paragraph(
        f"<b>Generated :</b> {report_time}",
        styles["Normal"]
    )
)

elements.append(
    Paragraph(
        f"<b>Overall Risk :</b> {dashboard['risk']}",
        styles["Normal"]
    )
)

elements.append(
    Paragraph(
        f"<b>Security Score :</b> {dashboard['security_score']}%",
        styles["Normal"]
    )
)

elements.append(Spacer(1, 25))

# -------------------------------------------------
# Executive Summary
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Executive Summary</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1, 10))

summary = f"""
APIHawk performed an automated API Security Assessment.

The scan analyzed <b>{dashboard['total_apis']}</b> APIs and detected
<b>{dashboard['shadow_apis']}</b> Shadow APIs,
<b>{dashboard['sensitive_apis']}</b> Sensitive APIs,
<b>{dashboard['owasp_findings']}</b> OWASP findings and
<b>{dashboard['jwt_issues']}</b> JWT Authentication Issue(s).

Overall Security Risk:
<b>{dashboard['risk']}</b>

Overall Security Score:
<b>{dashboard['security_score']}%</b>
"""

elements.append(
    Paragraph(
        summary,
        styles["BodyText"]
    )
)

elements.append(Spacer(1, 25))

# -------------------------------------------------
# Security Statistics
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Security Statistics</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1, 10))

stats = [

    ["Metric", "Value"],

    ["Total APIs", dashboard["total_apis"]],

    ["Shadow APIs", dashboard["shadow_apis"]],

    ["Sensitive APIs", dashboard["sensitive_apis"]],

    ["OWASP Findings", dashboard["owasp_findings"]],

    ["JWT Issues", dashboard["jwt_issues"]],

    ["Security Score", f"{dashboard['security_score']}%"],

    ["Overall Risk", dashboard["risk"]]

]

table = Table(
    stats,
    colWidths=[250,180]
)

table.setStyle(

    TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("BOTTOMPADDING",(0,0),(-1,0),10)

    ])

)

elements.append(table)

elements.append(Spacer(1,25))
# -------------------------------------------------
# Security Findings
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Security Findings</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1, 10))

findings_data = [

    ["Method", "Endpoint", "Risk", "Reason"]

]

for item in findings:

    findings_data.append([

        item["method"],

        item["endpoint"],

        item["risk"],

        item["reason"]

    ])

findings_table = Table(
    findings_data,
    colWidths=[60, 170, 70, 180]
)

findings_table.setStyle(

    TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),

        ("BOTTOMPADDING",(0,0),(-1,0),8)

    ])

)

elements.append(findings_table)

elements.append(Spacer(1,25))

# -------------------------------------------------
# Risk Distribution
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Risk Distribution</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1,10))

risk_table = Table(

    [

        ["Severity","Count"],

        ["Critical", dashboard["critical"]],

        ["High", dashboard["high"]],

        ["Medium", dashboard["medium"]],

        ["Low", dashboard["low"]]

    ],

    colWidths=[220,120]

)

risk_table.setStyle(

    TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkred),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

    ])

)

elements.append(risk_table)

elements.append(Spacer(1,25))

# -------------------------------------------------
# OWASP API Security Summary
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>OWASP API Security Summary</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1,10))

owasp_table = Table(

    [

        ["Check","Status"],

        ["Shadow API Discovery","Completed"],

        ["Risk Classification","Completed"],

        ["OWASP Findings", dashboard["owasp_findings"]],

        ["JWT Authentication Issues", dashboard["jwt_issues"]],

        ["Overall Risk", dashboard["risk"]],

        ["Security Score", f"{dashboard['security_score']}%"]

    ],

    colWidths=[260,180]

)

owasp_table.setStyle(

    TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkgreen),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

    ])

)

elements.append(owasp_table)

elements.append(Spacer(1,25))
# -------------------------------------------------
# Security Recommendations
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Security Recommendations</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1, 10))

recommendations = [

    "Remove undocumented Shadow APIs immediately.",

    "Protect sensitive endpoints using strong authentication and authorization.",

    "Enable API rate limiting for all public endpoints.",

    "Perform regular OWASP API Security assessments.",

    "Rotate JWT signing secrets periodically.",

    "Keep Swagger/OpenAPI documentation synchronized.",

    "Enable centralized logging and monitoring.",

    "Disable debug and administrative endpoints in production."

]

for rec in recommendations:

    elements.append(

        Paragraph(
            "• " + rec,
            styles["BodyText"]
        )

    )

elements.append(Spacer(1, 20))

# -------------------------------------------------
# Assessment Summary
# -------------------------------------------------

elements.append(
    Paragraph(
        "<b><font size='16'>Assessment Summary</font></b>",
        styles["Heading2"]
    )
)

elements.append(Spacer(1,10))

summary_table = Table(

    [

        ["Metric","Value"],

        ["Total APIs", dashboard["total_apis"]],

        ["Shadow APIs", dashboard["shadow_apis"]],

        ["Sensitive APIs", dashboard["sensitive_apis"]],

        ["OWASP Findings", dashboard["owasp_findings"]],

        ["JWT Issues", dashboard["jwt_issues"]],

        ["Security Score", f"{dashboard['security_score']}%"],

        ["Overall Risk", dashboard["risk"]]

    ],

    colWidths=[250,180]

)

summary_table.setStyle(

    TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.navy),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

    ])

)

elements.append(summary_table)

elements.append(Spacer(1,25))

# -------------------------------------------------
# Footer
# -------------------------------------------------

elements.append(

    Paragraph(
        "<b>APIHawk v2.0</b>",
        styles["Heading2"]
    )

)

elements.append(

    Paragraph(
        "Professional API Security Assessment Framework",
        styles["Normal"]
    )

)

elements.append(

    Paragraph(
        f"Generated : {report_time}",
        styles["Normal"]
    )

)

elements.append(

    Paragraph(
        "Developed by Sai Sandeep Gedela",
        styles["Normal"]
    )

)

elements.append(

    Paragraph(
        "© 2026 APIHawk. All Rights Reserved.",
        styles["Normal"]
    )

)

# -------------------------------------------------
# Build PDF
# -------------------------------------------------

doc.build(elements)

print("=" * 70)
print("🦅 APIHAWK PDF REPORT GENERATOR")
print("=" * 70)
print("✅ PDF Report Generated Successfully")
print(f"📄 Report : {report_path}")
print(f"📅 Generated : {report_time}")
print(f"📊 Security Score : {dashboard['security_score']}%")
print(f"🚨 Overall Risk : {dashboard['risk']}")
print("=" * 70)
