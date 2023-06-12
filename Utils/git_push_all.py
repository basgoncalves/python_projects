# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
import platform
from git_repos import import_repos
import re

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def summary_git_status(repo_directory):
    
    output = subprocess.run(["git", "status"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    string = output.stdout.decode('utf-8')
    # split based on the possible git status outputs: https://git-scm.com/docs/git-status
    parts = re.split(r'nM\t|nA\t|nD\t|nT\t|nR\t|nC\t|nU\t', string) # Split the string based on the delimiters using regular expression
    parts = [part for part in parts if part] # Remove empty strings from the list
    changes_summary = '\n'.join(parts) # Join the parts with newlines
    
    return changes_summary


repos = import_repos()        
# loop over the list of repos
for i in range(len(repos)):
    repo_directory = repos[i]
    os.chdir(repo_directory)
    
    time.sleep(0.5)
    output = subprocess.run(["git", "status"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    if output.stdout is not None and not str(output.stdout).__contains__('working tree clean'):
        print(summary_git_status(repo_directory))
        print('trying to push "' + repo_directory + '" ...')
        msg = input('Type the commit message (+ ENTER):') 
        
        # add all the files
        subprocess.run(["git", "add", "."], cwd=repo_directory)
        # commit file
        subprocess.run(["git", "commit", "-m", msg], cwd=repo_directory)
        # push
        subprocess.run(["git", "push"], cwd=repo_directory) 

        clear_terminal()

 