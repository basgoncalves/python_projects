import sys
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pandas as pd

# create a class for each option so that we can print the option names
class Option:
    def __init__(self, func):
        self.func = func

    def run(self):
        self.func()

#%% Options
def speed_test():
    import speedtest
    speed_test = speedtest.Speedtest()

    download_speed = round(speed_test.download()/1e6)
    print("Your Download speed is", download_speed,'Mb') 

    upload_speed = round(speed_test.upload()/1e6)
    print("Your Upload speed is", upload_speed,'Mb')

def get_current_dir():
    print("for .py")
    print("dir_path = os.path.dirname(os.path.realpath(__file__))")
    print("for ipynb")
    print("dir_path = os.getcwd()")

def python_path():
    print(sys.executable)

def print_python_libs():
    print(os.path.join(os.path.dirname(sys.executable),'Lib','site-packages'))

def files_above_100mb():
    
    current_path = os.getcwd()

    # User select the folder of the volume you want to convert folders
    target_path = askdirectory(initialdir=current_path)

    size_bytes = pd.DataFrame(columns=["file", "size"])
    count = -1

    for root, dirs, files in os.walk(target_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                size_in_mb = round(size / (1024 * 1024), 2)
                if size_in_mb > 100:
                    count += 1
                    # Remove common part of target_path from full_path
                    relative_path = os.path.relpath(full_path, target_path)
                    size_bytes.loc[count] = [relative_path, size_in_mb]

    # Display the resulting DataFrame
    print(size_bytes)

# print names (NOT AN OPTION)
def print_option_names():
    options = [name for name in globals() if isinstance(globals()[name], Option)]
    for option in options:
        print(option)

#%% Errors
def print_error_message():
    print("please select one of the following options:")
    print_option_names()
    print("eg usage: utils.py speet_test")

#%% Select
def select():
    # Check if the number of command line arguments is not equal to 2
    if len(sys.argv) != 2:
        print_error_message()
        sys.exit(1)

    # Get the command line argument
    option = sys.argv[1]

    # Check the value of the command line argument
    if option == "python_path":
        python_path.run()

    elif option == "python_libs":
        print_python_libs.run()

    elif option == "speed_test":
        speed_test.run()

    elif option == "get_current_dir":
        get_current_dir.run()

    elif option == "files_above_100mb":
        files_above_100mb.run()

    else:
        # Invalid command line argument
        print_error_message()
        sys.exit(1)

python_path = Option(python_path)
speed_test = Option(speed_test)
get_current_dir = Option(get_current_dir)
files_above_100mb = Option(files_above_100mb)

if __name__ == "__main__":
    select()