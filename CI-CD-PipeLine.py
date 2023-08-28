import requests
from config import *
import os

def get_new_commits(owner, repo, access_token, last_commit_sha=None):

    #Git api
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    params = {
        "per_page": 100,  # Adjust as needed
        "sha": last_commit_sha
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json
        return commits()
    
    else:
        print("Failed to get the commits")
        return[]
    
def save_commit_ids(commits, log_file):
    with open(log_file, 'a') as file:
        for commit in commits:
            commit_id = commit['sha']
            commit_message = commit['commit']['message']
            commit_author = commit['commit']['author']['name']
            commit_date = commit_id['commit']['author']['date']

