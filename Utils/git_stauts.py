# meaning of the status codes - https://git-scm.com/docs/git-status#_changed_tracked_entries
import subprocess
import sys
import os
import time
import re
from git_repos import import_repos


def split_changes_summary_in_different_lines(string):
    # split based on the possible git status outputs: https://git-scm.com/docs/git-status
    parts = re.split(r'nM\t|nA\t|nD\t|nT\t|nR\t|nC\t|nU\t', string) # Split the string based on the delimiters using regular expression
    parts = [part for part in parts if part] # Remove empty strings from the list
    result = '\n'.join(parts) # Join the parts with newlines
    return result

repos = import_repos()
exist_changes_to_commit = 0
dir_path = os.path.dirname(os.path.realpath(__file__)) # for .py
txt_file = os.path.join(dir_path, 'changes_summary.txt')

# empty file
with open(txt_file, 'w') as f:
    f.write(' ') 

# loop over the list 
for repo_directory in repos:
    os.chdir(repo_directory)
    time.sleep(0.75)
    # pull
    output = subprocess.run(["git", "status"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    if output.stdout is not None and not str(output.stdout).__contains__('working tree clean'):
        if exist_changes_to_commit == 0:
            print('these repos have unsolved commits')
            exist_changes_to_commit = 1
        print(repo_directory)
        # get commit summary
        changes_summary = subprocess.run(["git", "diff", "--name-status", "HEAD^"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        changes_summary = split_changes_summary_in_different_lines(changes_summary.stdout.decode('utf-8'))
        # print(changes_summary.stdout.decode('utf-8'))
        # write changes summary to text file
        with open(txt_file, 'a') as f:
            f.write(repo_directory + '\n') 
            f.write('\n')
            f.write(changes_summary)
            f.write('\n')
                
subprocess.Popen(["explorer", txt_file],creationflags=subprocess.DETACHED_PROCESS)

if exist_changes_to_commit == 0:
    print('all repos are up to date')
