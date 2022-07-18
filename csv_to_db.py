from multiprocessing import current_process
import pandas as pd
import sqlite3 
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from pathlib import Path

def csv_to_db(csv_filedir):

    if not Path(csv_filedir).is_file():
        current_path = os.getcwd()
        Tk().withdraw()                                     
        csv_filedir = askopenfilename(initialdir=current_path) 

    try:
        data = pd.read_csv(csv_filedir)
    except:
        print("Something went wrong when opening to the file")
        print(csv_filedir)

    df = pd.DataFrame(data)

    [path,filename] = os.path.split(csv_filedir)
    [filename,_] = os.path.splitext(filename)
    database_filedir = os.path.join(path, filename + '.db')

    if not os.path.exists(database_filedir):
        f = open(database_filedir, "x")

    conn = sqlite3.connect(database_filedir)
    df.to_sql(database_filedir, conn, if_exists='append', index=False)

    print('\n' + csv_filedir + ' \n converted to \n ' + database_filedir)

    return database_filedir