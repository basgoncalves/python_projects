import subprocess
from git_repos import import_repos
import os
# Change to the repository directory
repos = import_repos()
repo_directory = repos[0]
os.chdir(repo_directory)

# Pull the latest changes
output = subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the latest commit message
output = subprocess.run(["git", "log", "-1", "--pretty=format:%s"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
commit_message = output.stdout.decode().strip()

# Print the latest commit message
print(commit_message)