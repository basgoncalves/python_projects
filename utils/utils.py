import sys
import os

def speed_test():
    import speedtest
    speed_test = speedtest.Speedtest()

    download_speed = round(speed_test.download()/1e6)
    print("Your Download speed is", download_speed,'Mb') 

    upload_speed = round(speed_test.upload()/1e6)
    print("Your Upload speed is", upload_speed,'Mb')

def select():
    # Check if the number of command line arguments is not equal to 2
    if len(sys.argv) != 2:
        print("usage: setup.py option1 or option2")
        sys.exit(1)

    # Get the command line argument
    option = sys.argv[1]

    # Check the value of the command line argument
    if option == "python_path":
        print(sys.executable)

    elif option == "python_libs":
        print(os.path.join(os.path.dirname(sys.executable),'Lib','site-packages'))

    elif option == "speed_test":
        speed_test()

    else:
        # Invalid command line argument
        print("usage: setup.py option1 or option2")
        sys.exit(1)

if __name__ == "__main__":
    select()