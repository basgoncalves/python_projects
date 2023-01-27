# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform

device_details = platform.uname()
print(type(device_details))
msg = input('Which pc are you pulling to? (P = personal / W = work at uni vienna):') 

<<<<<<< HEAD
# list of directories where repos are stored depending on current local machine
if msg is 'P':
        repos =[r'C:\Users\Bas\Documents\Papers-Reviews',
=======
if msg == 'P':
        # list of repos in the current local machine
        repos =[r'C:\Users\Bas\Documents\Papers-Reviews\Reviews',
>>>>>>> 950796954d55ddd4282a25cfcf9bd87a7379bb65
                r'C:\Code\Git\Python_projects',
                r'C:\Code\Git\MSKmodelling']
elif msg == 'W':
        repos =[r'C:\Users\Biomech\Documents\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling']
else:
        print('Please write "W" or "P"')
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