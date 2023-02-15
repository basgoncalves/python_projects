from tkinter import Tk
from tkinter.filedialog import askopenfilename
import spicy
import os

 
current_path = os.getcwd()
Tk().withdraw()                                     
csv_filedir = askopenfilename(initialdir=current_path)    

data = spicy.io.loadmat()