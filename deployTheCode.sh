#!/bin/bash

# github and aws server local repo
github_repo="https://github.com/sayanalokesh/CI-CD-Pipeline_Tool.git"
aws_server_repo_path="/home/lokesh/CI-CD-Pipeline_Tool"

# Nginx server path for the index.html file
nginx_html_path="/var/www/autodeploy"

# Navigate to the local repository directory
cd $aws_server_repo_path

# Pull the latest changes from the GitHub repository
git pull

# Check if index.html has changed
if [[ $(git diff --name-only HEAD@{1} HEAD) =~ "index.html" ]]; then
    # Copy the updated index.html to the Nginx server path
    sudo cp index.html $nginx_html_path
    
    # Restart Nginx
    sudo systemctl restart nginx
