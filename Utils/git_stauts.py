import subprocess
import sys
import os
import time
from git_repos import import_repos

repos = import_repos()
exist_changes_to_commit = 0
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

if exist_changes_to_commit == 0:
    print('all repos re up to date')