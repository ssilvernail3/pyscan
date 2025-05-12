from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def generate_report(target, results, format="html"):
    """
    Generate a scan report in either HTML or PDF format.

    Args:
        target (str): The IP address that was scanned.
        results (list): A list of dictionaries with keys: port, banner, vulns.
        format (str): 'html' or 'pdf'.

    Returns:
        None
    """
    # Set up Jinja2 templating environment
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    # Render the report content
    rendered = template.render(target=target, results=results)

    # File name base
    filename = f"report_{target.replace('.', '_')}"

    # HTML output
    if format == "html":
        html_path = f"{filename}.html"
        with open(html_path, "w") as f:
            f.write(rendered)
        print(f"\n[✓] HTML report saved to {html_path}")

    # PDF output
    elif format == "pdf":
        html_path = f"{filename}.html"
        pdf_path = f"{filename}.pdf"

        # Save HTML first (used for conversion)
        with open(html_path, "w") as f:
            f.write(rendered)

        # Convert to PDF using WeasyPrint
        HTML(html_path).write_pdf(pdf_path)
        print(f"\n[✓] PDF report saved to {pdf_path}")

    else:
        print("[!] Unsupported report format. Please choose 'html' or 'pdf'.")