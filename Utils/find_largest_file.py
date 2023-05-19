# import packages
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import math

current_path = os.getcwd()

# User select the folder of the volume you want to convert folders
target_path = askdirectory(initialdir=current_path)

size_bytes = 0
selected_filename = ''
for root, dirs, files in os.walk(target_path):
    for filename in files:
        full_path = os.path.join(root, filename)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            if size > size_bytes:
                size_bytes = size
                selected_filename = full_path


# this is needed so the small pop up window doesnt appear - https://www.reddit.com/r/learnpython/comments/1htprb/how_do_i_close_tkfiledialog_a_little_window_with/
root = Tk()
root.withdraw()

print('largest file = ' + selected_filename)
size_in_mb = round(size_bytes / (1024 * 1024),2)
print('size = ' + str(size_in_mb) + ' Mb')
