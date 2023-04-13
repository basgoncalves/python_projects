# make sure to cd into the git repo foler

import subprocess
import sys
import os
import time
from git_repos import import_repos

repos = import_repos()

# loop over the list 
for repo_directory in repos:
    os.chdir(repo_directory)
    time.sleep(0.75)
    # pull
    subprocess.run(["git", "status"], cwd=repo_directory)
     

