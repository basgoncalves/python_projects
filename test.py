import subprocess
import sys
import os
import time
import re


def split_changes_summary_in_different_lines(string):
    # split based on the possible git status outputs: https://git-scm.com/docs/git-status
    parts = re.split(r'nM\t|nA\t|nD\t|nT\t|nR\t|nC\t|nU\t', string) # Split the string based on the delimiters using regular expression
    parts = [part for part in parts if part] # Remove empty strings from the list
    result = '\n'.join(parts) # Join the parts with newlines
    return result

exist_changes_to_commit = 0
dir_path = os.path.dirname(os.path.realpath(__file__)) # for .py
desktop_path = os.path.expanduser("~/Desktop")
txt_file = os.path.join(desktop_path, 'changes_summary.txt')

# empty file
with open(txt_file, 'w') as f:
    f.write(' ') 

repo_directory = r'C:\Git\Papers-Reviews'

os.chdir(repo_directory)
time.sleep(0.75)

# pull
output = subprocess.run(["git", "status"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
print(output.stdout.decode('utf-8'))

exit()
if output.stdout is not None and not str(output.stdout).__contains__('working tree clean'):
    if exist_changes_to_commit == 0:
        print('these repos have unsolved commits')
        exist_changes_to_commit = 1
    print(repo_directory)
    
    # get commit summary
    changes_summary = subprocess.run(["git", "diff", "--name-status", "HEAD^"], cwd=repo_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    changes_summary = split_changes_summary_in_different_lines(changes_summary.stdout.decode('utf-8'))
    print(changes_summary)