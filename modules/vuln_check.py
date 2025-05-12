import json
import os

def check_vulnerabilities(banner):
    """
    Check a service banner against a local CVE database for known vulnerabilities.

    Args:
        banner (str): The service banner string to evaluate.

    Returns:
        list: A list of matching CVE entries (dictionaries), or an empty list if none found.
    """
    results = []

    # Path to the local CVE database file
    db_path = os.path.join("data", "cve_db.json")

    try:
        # Load CVE entries from the JSON file
        with open(db_path, "r") as f:
            vuln_db = json.load(f)

        # Check each CVE entry to see if it matches the banner
        for entry in vuln_db:
            product = entry["product"].lower()
            version = entry["version"]

            # Match product name (case-insensitive) and exact version string
            if product in banner.lower() and version in banner:
                results.append(entry)

    except FileNotFoundError:
        print("[!] CVE database not found.")
    except Exception as e:
        print(f"[!] Error reading CVE database: {e}")

    return results