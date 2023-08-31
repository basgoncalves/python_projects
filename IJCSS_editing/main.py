# USAGE:
# just run the code and you will be asked to select the Volume folder 
# The assumption is that you have access to UniVienna Shared Drive "Z:\iacss\IACSS_IJCSS\IJCSS\Volumes"
# If you don't have access to it ask the IT office

import install_needed_pkg
import subprocess 
import aspose.words as aw
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from docx2pdf import convert
import shutil
import textract

def please_close_word():
    import pyautogui
    import time

    # Check if any Word documents are open
    while pyautogui.getWindowsWithTitle("Word"):
        # Ask the user to save and close all documents
        result = pyautogui.confirm(
            "Some Word documents are still open. Do you want to save and close them?",
            buttons=["Yes", "No"]
        )
        
        if result == "Yes":
            word_windows = pyautogui.getWindowsWithTitle("Word")
            # Press Alt+F4 to close all Word documents
            for window in word_windows:
                window.close()
            # pyautogui.hotkey("alt", "f4")
    
    # No Word documents are open
    pyautogui.alert("All Word documents are closed.")

please_close_word()

# if you want old files to be converted again, change to "True"
re_convert_files_that_already_exist = False

# User select the folder of the volume you want to convert folders 
volumes_path = askdirectory(initialdir=r'Z:\iacss\IACSS_IJCSS\IJCSS\Volumes')
word_path = os.path.join(volumes_path, r'3-Uploads\1-Word','')
pdf_path = os.path.join(volumes_path, r'3-Uploads\2-PDF_ausWord','')
ps_path = os.path.join(volumes_path,r'3-Uploads\3-PostScript','')
final_path = os.path.join(volumes_path, r'3-Uploads\4-PDF_ausPostScript','')

# open the progress file 
os.startfile(os.path.join(os.path.dirname (volumes_path), r'IJCSS - Progress_all.xlsx'))

# get volume and issue from folder name (must be in the format 'Vol222023Ed1')
volume = volumes_path.split(r'/')[-1].split('Vol')[1][0:2]
issue = volumes_path.split(r'/')[-1].split('Ed')[1][0:1]

# create final submission folder (will be used to zip in the end)
submit_folder = os.path.join(volumes_path, r'3-Uploads\10516-Volume{}-Issue{}'.format(volume,issue), '')

if not os.path.isdir(submit_folder):
    os.mkdir(submit_folder)

for path, subdirs, files in os.walk(word_path):
    for name in files:
        # For each file we find, we need to ensure it is a .docx file before adding
        #  it to our list
        try: 
            text = textract.process(os.path.join(path, name))
        except: 
            print('not able to open ' + os.path.join(path, name))
            continue
        
        if os.path.splitext(os.path.join(path, name))[1] == ".docx":
            word_file_path = os.path.join(path, name)
            
            # assign the names of each file format (pdf, ps, final_pdf)
            file_name, file_extension = os.path.splitext(word_file_path)
            pdf_file_path = os.path.join(pdf_path,name.replace(file_extension,'.pdf'))
            ps_file_path = os.path.join(ps_path,name.replace(file_extension,'.eps'))
            pdf_file_path_final = os.path.join(final_path,name.replace(file_extension,'.pdf'))
            submit_file_path_final = os.path.join(submit_folder,name.replace(file_extension,'.pdf'))
                    
             
            if not os.path.isfile(submit_file_path_final) or re_convert_files_that_already_exist == True:
                
                convert(word_file_path, pdf_file_path)                          # convert to PDF: "1-Word"
                
                subprocess.call(['pdf2ps', pdf_file_path, ps_file_path])        # convert to post script: "2-PDF_ausWord"
                
                subprocess.call(['ps2pdf', ps_file_path, pdf_file_path_final])  # convert to pdf again: "3-PostScript"
                
                shutil.copyfile(pdf_file_path_final, submit_file_path_final)    # copy pdf to the final location: "4-PDF_ausPostScript"

            

