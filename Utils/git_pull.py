# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time

# list of repos in the current local machine
repos =[r'C:\Users\Bas\Documents\Papers-Reviews\Reviews',
        r'C:\Code\Git\Python_projects',
        r'C:\Code\Git\MSKmodelling']

# loop over the list 
for repo_directory in repos:
    print('')
    print('pulling "' + repo_directory + '" ...')
    print('')
    time.sleep(0.9)
    # pull
    subprocess.run(["git", "pull"], cwd=repo_directory) 