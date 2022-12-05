import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import win32com.client


def convert_to_text(word_filedir):
    # Open the Word document
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(word_filedir)

    txt_filedir = word_filedir.replace('.docx','.txt')
    # Save the Word document as a text file
    doc.SaveAs(txt_filedir, 2) # 2 = wdFormatText
    doc.Close()    
    return txt_filedir

def convert_to_word(txt_filedir):
    
    word_filedir = txt_filedir.replace('.txt','_no_nums.docx')
    word = win32com.client.Dispatch("Word.Application")

    # Create a new Word document
    doc = word.Documents.Add()

    # Open the text file and read its contents
    with open(txt_filedir, "r") as file:
        text = file.read()

    # Insert the text into the Word document
    doc.Range().InsertAfter(text)

    # Save the Word document
    doc.SaveAs(word_filedir)

    # Close the Word document and Word
    doc.Close()
    word.Quit()    
    os.remove(txt_filedir)


os.system('cls' if os.name == 'nt' else 'clear')
current_path = os.getcwd()
Tk().withdraw()                                     
word_filedir = askopenfilename(initialdir=current_path)           

txt_filedir = convert_to_text(word_filedir)

num_lines = 0

with open(txt_filedir) as fp:
    for line in fp:
            num_lines += 1

print(line)
print('number lines = ', num_lines)

convert_to_word(txt_filedir)






  # # Open the text file and save it as a Word document
    # word = win32com.client.Dispatch("Word.Application")
    # text_doc = word.Documents.Open(txt_filedir)
    # text_doc.SaveAs(word_filedir)
    # text_doc.Close()

    # # Close Word
    # word.Quit()