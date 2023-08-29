import requests
from config import *
import os

# defining the Git repo details to check the commit id's using API
def get_new_commits(owner, repo, access_token, last_commit_sha):

    # Git api
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    # Authorizing the token details
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # The parameters help in fetching commits in batches and starting from a specific commit. In this case, I've mentioned the first commit performed to the repo.
    params = {
        "per_page": 100,  # Adjust as needed. This parameter specifies the number of commits to be returned per page. I've set the requests to 100, which means the API will return up to 100 commits in a single response.
        "sha": last_commit_sha
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()
        return commits
    
    else:
        print("Failed to get the commits")
        return[]
    
def check_index_html_update(commits):
    for commit in commits:
        commit_hash = commit['sha']
        files_changed = commit.get('files', [])

        print(f"Commit Hash: {commit_hash}")
        print("Files Changed:", [file['filename'] for file in files_changed])
        
        for file in files_changed:
            if file.get('filename') == 'index.html':
                print("Found index.html change.")
                return True
    return False

def save_commit_ids(commits, log_file):  #save the commits performed on the index file into log_file
    with open(log_file, 'a') as file:
        for commit in commits:
            commit_id = commit['sha']
            commit_message = commit['commit']['message']
            commit_author = commit['commit']['author']['name']
            commit_date = commit['commit']['author']['date']

            log_entry = f"Commit Hash: {commit_id}\nAuthor: {commit_author}\nDate: {commit_date}\nMessage: {commit_message}\n\n"
            file.write(log_entry)

def main():
      
    last_commit_sha = '2ef80533b644bbe50207cce6692f73a900708037'
    log_file = 'commit_log.txt'
    
    commits = get_new_commits(owner, repo, access_token, last_commit_sha)
        
    if commits:
        print(f"Commits {commits}")
        if check_index_html_update(commits):
            save_commit_ids(commits, log_file)
            print(f"Saved {len(commits)} commits to {log_file}.")
        else:
            print("No new commit id found and index file is not updated.")
    else:
        print("No new commits found.")

if __name__ == "__main__":
    main()
    
# def save_commit_ids(commits, log_file):  #save the commits performed on the index file into log_file
#     with open(log_file, 'a') as file:
#         for commit in commits:
#             commit_id = commit['sha']
#             commit_message = commit['commit']['message']
#             commit_author = commit['commit']['author']['name']
#             commit_date = commit['commit']['author']['date']

#             log_entry = f"Commit Hash: {commit_id}\nAuthor: {commit_author}\nDate: {commit_date}\nMessage: {commit_message}\n\n"
#             file.write(log_entry)

# def main():
    
#     last_commit = '2ef80533b644bbe50207cce6692f73a900708037'

#     log_file = 'commit_log.txt'

#     commits = get_new_commits(owner, repo, access_token, last_commit)

#     if commits:
#         save_commit_ids(commits, log_file)
#         print(f"Found new commit and saved {len(commits)} commits to {log_file}.")

#     else:
#         print("No new commits found.")

# if __name__ == "__main__":
#     main()