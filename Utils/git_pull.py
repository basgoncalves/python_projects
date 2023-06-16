# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform
from git_repos import import_repos

repos = import_repos()
print(repos)
        
desktop_path = os.path.expanduser("~/Desktop")
txt_file = os.path.join(desktop_path, 'changes_summary.txt')

# empty file
with open(txt_file, 'w') as f:
    f.write(' ')         
        
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
                output = subprocess.run(["git", "log", "-1", "--pretty=format:%s"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                commit_message = output.stdout.decode().strip()
                output_dict[repo_directory] = commit_message
        else:
                output_dict[repo_directory] = 'none'
    except subprocess.CalledProcessError as e:
        output_dict[repo_directory] = e
    except FileNotFoundError as e:
        output_dict[repo_directory] = e
    except Exception as e:
        output_dict[repo_directory] = e
        
    # print(changes_summary.stdout.decode('utf-8')) write changes summary to text file
    with open(txt_file, 'a') as f:
        f.write(repo_directory + '\n') 
        f.write('\n')
        f.write(output_dict[repo_directory] )
        f.write('\n')

for key, value in output_dict.items():
    print(f"{key}: {value}")
