# meaning of the status codes - https://git-scm.com/docs/git-status#_changed_tracked_entries
import subprocess
import sys
import os
import time
import re
from git_tools import import_repos,split_changes_summary_in_different_lines

repos = import_repos()
exist_changes_to_commit = 0
dir_path = os.path.dirname(os.path.realpath(__file__)) # for .py
desktop_path = os.path.expanduser("~/Desktop")
txt_file = os.path.join(desktop_path, 'changes_summary.txt')

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
        changes_summary = split_changes_summary_in_different_lines(output.stdout.decode('utf-8'))
        
        # print(changes_summary.stdout.decode('utf-8')) write changes summary to text file
        with open(txt_file, 'a') as f:
            f.write(repo_directory + '\n') 
            f.write('\n')
            f.write(changes_summary)
            f.write('\n')
            f.write('======================================================================= \n')
                
if exist_changes_to_commit == 0:
    print('all repos are up to date')
else:
    answer = input('do you want to push all these repos? (y/n)  ')
    
    if answer == 'y':
        import git_push_all
    
    
os.startfile(txt_file)
