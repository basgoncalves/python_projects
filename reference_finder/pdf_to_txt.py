import PyPDF2
import os
from tkinter import filedialog
from tkinter import Tk


def extract_references_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        references = []

        for page_num in range(num_pages):
            page = reader.pages[page_num] 
            text = page.extract_text()
            lines = text.split('\n')
            in_references_section = False
            for line in lines:
                if 'Table of Contents' in line or 'TABLE OF CONTENTS' in line:
                    break
                if 'References' in line or 'REFERENCES' in line:
                    in_references_section = True
                if in_references_section:
                    references.append(line.split('  '))

    with open(txt_path, 'w') as txt_file:
        for reference in references:
            txt_file.write('\n'.join(reference) + '\n')
            
    print(f"References have been saved to {txt_path}")

if __name__ == "__main__":
    pdf_path = filedialog.askopenfilename()
    txt_path = os.path.splitext(pdf_path)[0] + '.txt'
    extract_references_from_pdf(pdf_path, txt_path)