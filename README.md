# 🔍 PyScan - Lightweight Python Vulnerability Scanner

**PyScan** is a Python-based vulnerability scanner that scans a target IP for open ports, grabs banners to identify running services, matches against known CVEs, and outputs a clean HTML report.

This is an in-progress cybersecurity project built to demonstrate both software engineering and security fundamentals — with more features actively in development.

🚧 **Upcoming Enhancements:**
- Multi-threaded port scanning
- PDF and CSV report export
- Shodan & NVD API integration
- Flask-based web interface
- CLI packaging for pip install

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


