import json
import ast
from fpdf import FPDF
from datetime import datetime

def parse_input_and_create_pdf(input_data):
    # Step 1: Parse the JSON-like input
    try:
        data = ast.literal_eval(input_data)
    except Exception as e:
        return f"Error parsing input: {str(e)}"
    
    # Step 2: Extract the list of SOC-2 compliant services
    services = data.get('result', '')

    # Create a new FPDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    # Add a title
    pdf.cell(200, 10, 'List of AWS SOC-2 Compliant Services', 0, 1, 'C')
    
    # Add each service to the PDF
    services_lines = services.split('\n')
    for line in services_lines:
        if line.strip():
            pdf.cell(200, 10, line, 0, 1)


    # Save the PDF
    started_at = datetime.now().strftime("%Y%m%d_%H%M%S")  # Formats the date and time in a file-friendly manner
    file_name = f'/Users/sakom/github/hackathon05122024/safescale/ui/public/pdfs/evidence_doc_{started_at}.pdf'
    pdf.output(file_name)
    return "Evidence created successfully"