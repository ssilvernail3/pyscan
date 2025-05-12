# 🔍 PyScan - Lightweight Python Vulnerability Scanner

PyScan is a simple, Python-based vulnerability scanner designed to scan a target IP address for open ports, identify running services, detect known vulnerabilities, and generate a clean HTML report.

This project was built to demonstrate both software development and cybersecurity skills, including banner grabbing, CVE detection, and report generation.

---

## ⚙️ Features

- TCP port scanning using Python sockets
- Banner grabbing to fingerprint open services
- Local CVE lookup using a JSON vulnerability database
- HTML report generation with Jinja2 templating
- Clean CLI interface using `argparse`

---

## 🚀 Getting Started

1. Clone the Repo

- git clone https://github.com/yourusername/pyscan.git
- cd pyscan 


1. Install Jinja2

- pip3 install jinja2 

3. Run the scanner

- python3 pyscan.py --target 127.0.0.1 --report html

---

 📁 Project Structure 

pyscan/
├── pyscan.py                 # Main script
├── modules/
│   ├── scanner.py            # Handles port scanning
│   ├── banner.py             # Grabs service banners
│   ├── vuln_check.py         # Checks for known CVEs
│   └── report_gen.py         # Generates HTML report
├── data/
│   └── cve_db.json           # Local CVE database
├── templates/
│   └── report_template.html  # Jinja2 template for reports
└── README.md

🛡️ CVE Database Format

[
  {
    "product": "SimpleHTTP",
    "version": "0.6",
    "cve": "CVE-2022-23943",
    "description": "Directory traversal via crafted URLs.",
    "severity": "Medium"
  }
]

📄 Sample Output

The HTML report includes:
	•	Target IP
	•	List of open ports
	•	Service banners
	•	Any matched vulnerabilities (CVE ID, description, severity)

Just open the report file in a browser to view results.

👨‍💻 Author

Shane Silvernail
Cybersecurity & Software Engineering


