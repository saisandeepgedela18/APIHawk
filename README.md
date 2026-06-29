# 🦅 APIHawk v2.0

### Professional API Security Assessment Framework

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v2.0-orange)

---

## 🌐 Live Demo

### 🚀 Try APIHawk Online

**🔗 https://apihawk-security-dashboard.streamlit.app**

---

## 📖 Overview

APIHawk is a professional API Security Assessment Framework developed using Python.

The framework automatically analyzes OpenAPI/Swagger specifications to discover APIs, identify sensitive endpoints, detect Shadow APIs, classify security risks, analyze JWT authentication, and generate professional security reports.

APIHawk provides an interactive Streamlit dashboard together with HTML and PDF reporting for comprehensive API security assessment.

---

## ✨ Features

- 🔍 API Discovery
- 👤 Shadow API Detection
- 🛡️ Sensitive Endpoint Detection
- 📊 Risk Classification Engine
- 🔐 JWT Authentication Analyzer
- 🛡️ OWASP API Security Analysis
- 🗄️ SQLite Database Integration
- 📈 Interactive Streamlit Dashboard
- 📄 Professional HTML Reports
- 📕 Professional PDF Reports
- ⚡ Live API Assessment

---

## 🏗️ System Architecture

```
                Swagger / OpenAPI
                        │
                        ▼
               API Discovery Engine
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Shadow APIs     Sensitive APIs     Risk Engine
        │               │               │
        └───────────────┼───────────────┘
                        ▼
              SQLite Security Database
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Dashboard        HTML Report      PDF Report
```
---

# 📂 Project Structure

```
APIHawk/
│
├── dashboard/
│   ├── dashboard.py
│   └── dashboard_data.py
│
├── database/
│   └── apihawk.db
│
├── datasets/
│
├── docs/
│
├── reports/
│   ├── security_report.html
│   └── security_report.pdf
│
├── screenshots/
│
├── src/
│   ├── api_discovery.py
│   ├── database_manager.py
│   ├── endpoint_comparison.py
│   ├── endpoint_enumerator.py
│   ├── html_report_generator.py
│   ├── jwt_analyzer.py
│   ├── live_api_scanner.py
│   ├── log_parser.py
│   ├── owasp_engine.py
│   ├── pdf_report_generator.py
│   ├── report_generator.py
│   ├── risk_classifier.py
│   ├── risk_engine.py
│   ├── risk_scoring.py
│   ├── security_headers.py
│   ├── security_service.py
│   ├── sensitive_endpoint_detector.py
│   ├── shadow_api_detector.py
│   ├── swagger_parser.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Streamlit | Interactive Dashboard |
| SQLite | Security Findings Database |
| ReportLab | PDF Report Generation |
| HTML/CSS | HTML Report Generation |
| Pandas | Data Processing |
| Matplotlib | Data Visualization |
| OpenAPI / Swagger | API Specification Parsing |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/saisandeepgedela18/APIHawk.git
```

Move into the project

```bash
cd APIHawk
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running APIHawk

### Launch Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

### Generate HTML Report

```bash
python src/html_report_generator.py
```

---

### Generate PDF Report

```bash
python src/pdf_report_generator.py
```

---

# 📊 Modules

| Module | Status |
|---------|--------|
| API Discovery | ✅ |
| Shadow API Detection | ✅ |
| Sensitive Endpoint Detection | ✅ |
| Risk Classification | ✅ |
| OWASP API Security Analysis | ✅ |
| JWT Authentication Analyzer | ✅ |
| SQLite Database | ✅ |
| HTML Report Generator | ✅ |
| PDF Report Generator | ✅ |
| Interactive Dashboard | ✅ |

---

# 📸 Project Screenshots

## Project Structure
![Project Structure](screenshots/01_project_structure.png.png)

## Source Modules
![Source Modules](screenshots/02_source_modules.png.png)

## API Discovery
![API Discovery](screenshots/03_api_discovery_output.png.png)

## Endpoint Enumeration
![Endpoint Enumeration](screenshots/04_endpoint_enumeration.png.png)

## Security Header Analysis
![Security Headers](screenshots/05_security_headers.png.png)

## Risk Scoring
![Risk Scoring](screenshots/06_risk_scoring.png.png)

## Authentication Detector
![Authentication Detector](screenshots/09_Authentication_Detector_Output.png.png)

## OpenAPI Analyzer
![OpenAPI Analyzer](screenshots/10_OpenAPI_Analyzer_Output.png.png)

## Shadow API Detection
![Shadow API Detector](screenshots/11_Advanced_Shadow_API_Detector_Output.png.png)

## Sensitive Endpoint Detection
![Sensitive Endpoint Detector](screenshots/12_Sensitive_Endpoint_Detector_Output.png.png)

## Risk Classification Engine
![Risk Classification](screenshots/13_Risk_Classification_Engine_Output.png.png)

## SQLite Database
![SQLite Database](screenshots/14_SQLite_Database_Output.png.png)

## Interactive Dashboard
![Dashboard](screenshots/15_Streamlit_Dashboard.png.png)

## Professional HTML Report
![Professional HTML Report](screenshots/17_Professional_HTML_Report.png.png)

## Professional PDF Report
![Professional PDF Report](screenshots/19_Professional_PDF_Report.png.png)

## Dynamic Analytics Dashboard
![Analytics Dashboard](screenshots/20_Dynamic_Analytics_Dashboard.png.jpeg)

## Live API Scanner
![Live API Scanner](screenshots/21_Live_API_Scanner_Output.png.png)

### HTML Report Preview

![HTML Report - Page 1](screenshots/Screenshot%20(156).png)

![HTML Report - Page 2](screenshots/Screenshot%20(157).png)

![HTML Report - Page 3](screenshots/Screenshot%20(158).png)


## 📕 PDF Security Report

```markdown
![PDF Report](screenshots/pdf_report.png)
```

---

## 🔍 Live API Scanner

```markdown
![Scanner](screenshots/scanner.png)
```
---

# 🛣️ Roadmap

### Upcoming Features

- 🤖 AI-Based Risk Scoring
- 🐳 Docker Deployment
- ☁️ Cloud Security Assessment
- 🔄 CI/CD Security Integration
- 📡 Continuous API Monitoring
- 🔗 Burp Suite Integration
- 🌐 CVE & Threat Intelligence Integration
- 📱 REST API for APIHawk
- 📈 Advanced Security Analytics
- 🔔 Real-Time Security Alerts

---

# 📊 Sample Output

APIHawk automatically generates professional security reports.

### Dashboard

- Interactive Streamlit Dashboard
- Real-time Security Metrics
- API Inventory
- Risk Distribution
- Security Score

### HTML Report

- Executive Summary
- Security Findings
- Risk Distribution
- OWASP API Security Summary
- Security Recommendations

### PDF Report

- Professional Printable Report
- Security Statistics
- Executive Summary
- Findings
- Assessment Summary

---

# 🔒 Security Checks Performed

✔ API Discovery

✔ Shadow API Detection

✔ Sensitive Endpoint Detection

✔ Risk Classification

✔ OWASP API Security Analysis

✔ JWT Authentication Analysis

✔ SQLite Security Logging

✔ HTML Report Generation

✔ PDF Report Generation

✔ Interactive Dashboard

---

# 👨‍💻 Author

## Sai Sandeep Gedela

**Computer Science Engineering Student**

Andhra University College of Engineering

### Connect with Me

- GitHub: https://github.com/saisandeepgedela18
- LinkedIn: https://www.linkedin.com/in/sai-sandeep-gedela-196754375?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the project

🛡️ Share it with the cybersecurity community

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

Special thanks to:

- Streamlit
- Python Community
- OWASP Foundation
- OpenAPI Initiative
- ReportLab
- SQLite
- Matplotlib
- Pandas

for providing excellent open-source technologies that made APIHawk possible.

---

<div align="center">

# 🦅 APIHawk v2.0

### Professional API Security Assessment Framework

**Developed by Sai Sandeep Gedela**

⭐ **If you like this project, don't forget to Star the repository!** ⭐

</div>
