import argparse
from modules.scanner import scan_ports
from modules.banner import grab_banner
from modules.vuln_check import check_vulnerabilities
from modules.report_gen import generate_report

""" PyScan - Lightweight Vulnerability Scanner
------------------------------------------
This script scans a given IP address for open ports, grabs service banners,
checks for known vulnerabilities using a local CVE database, and generates an HTML report.

Modules used:
- scanner.py for port scanning
- banner.py for banner grabbing
- vuln_check.py for CVE detection
- report_gen.py for HTML report output """


def main():

    # Main function that runs the PyScan vulnerability scanner. 
    # Parses command-line arguments, scans the target, checks for vulnerabilities, and generates an HTML report. 

    parser = argparse.ArgumentParser(description="PyScan - Lightweight Vulnerability Scanner")
    parser.add_argument("--target", required=True, help="Target IP address or range")
    parser.add_argument("--report", choices=["html", "pdf"], default="html", help="Report format")
    args = parser.parse_args()

    print(f"[*] Scanning target: {args.target}")
    print(f"[*] Report will be generated in: {args.report.upper()} format")

    # Scan a list of common open ports on the target IP

    open_ports = scan_ports(args.target, [22, 80, 443, 3306, 8080])

    scan_results = []

    if open_ports:
        print(f"\n[+] Open Ports and Services on {args.target}:")
        for port in open_ports:

            # Get the banner for each open port

            banner = grab_banner(args.target, port)
            clean_banner = banner.replace("\r", "").replace("\n", " | ")
            print(f"    - Port {port}: {clean_banner}")

            # Check for known vulnerabilities based on the banner 

            vulns = check_vulnerabilities(banner)
            if vulns:
                print(f"      ⚠️  Vulnerabilities Detected:")
                for v in vulns:
                    print(f"         - [{v['cve']}] {v['description']} (Severity: {v['severity']})")
            
            # Save the result for the final report

            scan_results.append({
                "port": port,
                "banner": banner,
                "vulns": vulns
            })
    else:
        print(f"\n[!] No open ports found on {args.target}.")

    # Generate an HTML report from the scan results
    
    generate_report(args.target, scan_results, args.report)

    print("\n[✓] Scan complete.")

if __name__ == "__main__":
    main()