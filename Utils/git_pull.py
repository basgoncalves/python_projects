# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform

device_details = platform.uname()

# list of directories where repos are stored depending on current local machine
if device_details.node == 'Bas-PC':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling',
                r'C:\Git\msk_modelling_python']
elif device_details.node == 'DESKTOP-8KRF896':
        repos =[r'C:\Git\Papers-Reviews',
                r'C:\Git\Python_projects',
                r'C:\Git\MSKmodelling',
                r'C:\Git\msk_modelling_python']
else:
        print('Current machine not configured. Add folder paths to the script or perform "git pull manually"')
        exit()
        
# loop over the list 
output_dict = {}
print('')
for i in range(len(repos)):
    repo_directory = repos[i]
    print('pulling "' + repo_directory + '" ...')
    time.sleep(0.5)
    
    # pull and handle errors 
    try:
        output = subprocess.run(["git", "pull"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        if output.stdout is not None:
                output_dict[repo_directory] = output.stdout.strip()
        else:
                output_dict[repo_directory] = 'none'
    except subprocess.CalledProcessError as e:
        output_dict[repo_directory] = e
    except FileNotFoundError as e:
        output_dict[repo_directory] = e
    except Exception as e:
        output_dict[repo_directory] = e
    
for key, value in output_dict.items():
    print(f"{key}: {value}")
