import sys
import os

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

def print_python_path():
    print(sys.executable)

def print_python_libs():
    print(os.path.join(os.path.dirname(sys.executable),'Lib','site-packages'))

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
        print_python_path()

    elif option == "python_libs":
        print_python_libs()

    elif option == "speed_test":
        speed_test()

    else:
        # Invalid command line argument
        print_error_message()
        sys.exit(1)

speed_test = Option(speed_test)
get_current_dir = Option(get_current_dir)

if __name__ == "__main__":
    select()