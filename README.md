# CI-CD-Pipeline_Tool
Creating a CI-CD pipeline without using DevOps tools such as Jenkins, CircleCI etc. I have used Python and Bash script to deploy a webserver.

# Contents

- [Task 1: Set Up a Simple HTML Project](#task-1-set-up-a-simple-html-project)
- [Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx](#task-2-set-up-an-aws-ec2local-linux-instance-with-nginx)
- [Task 3: Write a Python Script to Check for New Commits](#task-3-write-a-python-script-to-check-for-new-commits)
- [Task 4: Write a Bash Script to Deploy the Code](#task-4-write-a-bash-script-to-deploy-the-code)
- [Task 5: Set Up a Cron Job to Run the Python Script](#task-5-set-up-a-cron-job-to-run-the-python-script)
- [Task 6: Test the Setup](#task-6-test-the-setup)

## Task 1: Set Up a Simple HTML Project
1. Create a new GitHub repository and clone the repo.
2. Create a new HTML project with our desired content.
3. Add and commit our HTML files to the repository.
4. Push the index file to the GitHub repository.

## Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
1. Launch an AWS EC2 instance or set up a local Linux server. In my case, I have launched an EC2 instance.
2. Install Nginx on the instance with the command `sudo apt-get install nginx`.
3. Configure Nginx to serve our HTML project.
4. You can find the complete configuration of the Nginx and the HTML file in my GitHub repo. To check please click [here](https://github.com/sayanalokesh/herovired_devops_assignment.git) and go to the Networkings&Servers find Assignment_3.pdf.

## Task 3: Write a Python Script to Check for New Commits
1. Create a Python script that uses the GitHub API to check for new commits in our GitHub repository.
2. This script can make HTTP requests to the GitHub API and parse the response to detect new commits.
3. We will call the bash script whenever a new commit is detected to perform some tasks. The tasks are explained below.
4. The detailed explanation is provided in the script. Please open the code `CI-CD-PipeLine.py`.

## Task 4: Write a Bash Script to Deploy the Code
1. We create a Bash script that will clone the latest code from our GitHub repository to our server. If there is a repo, the code will pull the code and copy the index file to the desired path.
2. Once the index file is copied with the new code to the desired folder, the code restarts Nginx to reflect changes.

## Task 5: Set Up a Cron Job to Run the Python Script
1. To automate this process, we need to create a cron job on our server to run the Python script at regular intervals.
2. The Python script will periodically check for new commits, triggering the deployment script if there are new changes.

## Task 6: Test the Setup
1. To test this code, make a new commit to our GitHub repository by changing something to the index file.
2. Observe that the Python script detects the new commit.
3. The deployment script is triggered, updating our HTML project on the server.
4. Check that the changes are automatically reflected on the Nginx-served website.

This sequence of tasks outlines a basic continuous deployment pipeline for our HTML project, allowing you to automatically update our website whenever there are new commits to the GitHub repository.
