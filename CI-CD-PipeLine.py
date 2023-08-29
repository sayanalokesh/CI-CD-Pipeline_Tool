import os
import requests
from config import *

# providing the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# API URL to get latest commit
url = f'https://api.github.com/repos/{owner}/{repo}/branches/{branch}' # url of the repo from where we are getting the details
response = requests.get(url, headers=headers) # I'm asking to get the details from the page and authorising the page with the access token, once I get the response and asking to store in the variable

if response.status_code == 200: # we have the get response and asking to check the below details
   
    latest_commit_hash = response.json()['commit']['sha'] # I'm asking to check the 'sha' from the 'commit'
    
else:

    print("Error fetching commit hash:", response.text)
    latest_commit_hash = None

# Check if there's a new commit
previous_commit_hash_file = 'previous_commit_hash.txt' # assigning the file name(previous_commit_hash.txt) which is a string to the variable previous_commit_hash_file(it won't check for the content of the file)

# Below 3 lines will read the content of the file which is stored in previous_commit_hash_file variable and in the 2nd line it stores the content of the file in previous_commit_hash variable
if os.path.exists(previous_commit_hash_file):
    with open(previous_commit_hash_file, 'r') as file: 
        previous_commit_hash = file.read().strip()
else:
    previous_commit_hash = None
    
# If latest_commit_hash is defined and is not null and is not equal to previous_commit_hash
if latest_commit_hash and latest_commit_hash != previous_commit_hash:
    print("New commit detected:", latest_commit_hash)
    
    with open(previous_commit_hash_file, 'w') as file:
        file.write(latest_commit_hash + '\n')

else:
    print("No new commits or no update in index.html file.")