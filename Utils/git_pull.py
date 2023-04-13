# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform
from git_repos import import_repos

repos = import_repos()
print(repos)
        
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
