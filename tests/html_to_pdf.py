import pdfkit
# still need to install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html and add it to the PATH

def convert_html_to_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file,)
        print("HTML converted to PDF successfully!")
    except Exception as e:
        print(f"Error converting HTML to PDF: {str(e)}")

# Example usage
html_file = r"C:\Users\Bas\Desktop\test.html"
pdf_file = r"C:\Users\Bas\Desktop\test.pdf"
convert_html_to_pdf(html_file, pdf_file)