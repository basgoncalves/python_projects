# make sure all packages are installed 
import install_needed_pkg

# import packages
import subprocess 
import aspose.words as aw
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from docx2pdf import convert
import shutil
import textract


# User select the folder of the volume you want to convert folders 
volumes_path = askdirectory(initialdir=r'Z:\iacss\IACSS_IJCSS\IJCSS\Volumes')
word_path = os.path.join(volumes_path, r'3-Uploads\1-Word','')
pdf_path = os.path.join(volumes_path, r'3-Uploads\2-PDF_ausWord','')
ps_path = os.path.join(volumes_path,r'3-Uploads\3-PostScript','')
final_path = os.path.join(volumes_path, r'3-Uploads\4-PDF_ausPostScript','')

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
            
            # convert to PDF
            if not os.path.isfile(pdf_file_path):
                convert(word_file_path, pdf_file_path) 
            
            # convert to post script
            if not os.path.isfile(ps_file_path):
                subprocess.call(['pdf2ps', pdf_file_path, ps_file_path])          
            
            # convert to pdf again (final)
            if not os.path.isfile(pdf_file_path_final):
                subprocess.call(['ps2pdf', ps_file_path, pdf_file_path_final])
            
            # copy pdf to the final location 
            if not os.path.isfile(submit_file_path_final):   
                shutil.copyfile(pdf_file_path_final, submit_file_path_final)

                

# select documents to ad to specification document

# create folder 10516-VolumeXX-IssueY_Z

