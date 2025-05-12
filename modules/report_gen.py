from jinja2 import Environment, FileSystemLoader
import os

def generate_report(target, results, format="html"):

    """
    Generate an HTML report of the scan results using a Jinja2 template.

    Args:
        target (str): The IP address that was scanned.
        results (list): A list of dictionaries with keys: port, banner, and vulns.
        format (str): Report format ("html" currently supported).

    Returns:
        None
    """
    # Set up Jinja2 to load templates from the 'templates/' folder
    env = Environment(loader=FileSystemLoader("templates"))
    
    #Load the report HTML template
    template = env.get_template("report_template.html")

    # Render teh template from your scan data
    output = template.render(target=target, results=results)

    #Format the filename safely (replace . with _)
    output_path = f"report_{target.replace('.', '_')}.html"
    
    # Save the rendered HTML to a file
    with open(output_path, "w") as f:
        f.write(output)

    print(f"\n[✓] Report saved to {output_path}")