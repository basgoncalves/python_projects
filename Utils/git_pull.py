# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform

device_details = platform.uname()

# list of directories where repos are stored depending on current local machine
if device_details.node == 'Bas-PC':
        repos =[r'C:\Code\Git\Papers-Reviews',
                r'C:\Code\Git\Python_projects',
                r'C:\Code\Git\MSKmodelling']
elif device_details.node == 'DESKTOP-8KRF896':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling']
else:
        print('Current machine not configured. Add folder paths to the script or perform "git pull manually"')
        exit()
        
# loop over the list 
for repo_directory in repos:
    print('')
    print('pulling "' + repo_directory + '" ...')
    print('')
    time.sleep(0.75)
    # pull
    subprocess.run(["git", "pull"], cwd=repo_directory) 

# # clear console
# clear = lambda: os.system('cls')
# clear()

print('Everything is up to date')