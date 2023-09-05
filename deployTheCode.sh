#!/bin/bash

# GitHub repository URL
github_repo="https://github.com/sayanalokesh/CI-CD-Pipeline_Tool.git"

# Local repository path
local_repo_path="/home/lokesh/CI-CD-Pipeline_Tool"

# Nginx server path for the index.html file
nginx_html_path="/var/www/autodeploy"  # Replace with your actual Nginx server path

# Check if the local repository exists
if [ ! -d "$local_repo_path" ]; then
    # If the local repository doesn't exist, clone it
    git clone "$github_repo" "$local_repo_path"
else
    # Navigate to the local repository directory
    cd "$local_repo_path"

    # Pull the latest changes
    git pull

    # Copy the updated index.html to the Nginx server path
    sudo cp index.html "$nginx_html_path"

    # Restart Nginx to reflect changes
    sudo systemctl restart nginx
fi







# -cron job = * * * * * /usr/bin/python3 /home/lokesh/CI-CD-Pipeline_Tool/CI-CD-PipeLine.py
