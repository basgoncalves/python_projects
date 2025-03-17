import tkinter as tk
from tkinter import filedialog
import docx
import unidecode

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    return file_path

def extract_references(doc_path):
    doc = docx.Document(doc_path)
    references = []
    in_references_section = False

    for para in doc.paragraphs:
        if 'References' in para.text:
            in_references_section = True
        elif in_references_section and para.text.strip() == '':
            break
        elif in_references_section:
            references.append(para.text)

    return references

def save_references(references, doc_path):
    txt_path = doc_path.replace('.docx', '_references.txt')
    with open(txt_path, 'w') as f:
        for ref in references:
            # replace non-breaking space with regular space
            ref = unidecode.unidecode(ref)
            f.write(ref + '\n')

if __name__ == "__main__":
    doc_path = select_file()
    if doc_path:
        references = extract_references(doc_path)
        save_references(references, doc_path)
        print(f"References have been saved to {doc_path.replace('.docx', '_references.txt')}")
    else:
        print("No file selected.")