import os
import requests
import sys

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"

def create_pull_request(token, owner, repo, base_branch, head_branch, pr_title, pr_body):
    """Creates a new pull request on GitHub.
    
    Args:
        token (str): GitHub authentication token.
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        base_branch (str): The name of the branch you want the changes pulled into.
        head_branch (str): The name of the branch where your changes are implemented.
        pr_title (str): The title of the pull request.
        pr_body (str): The contents of the pull request.
    
    Returns:
        None: This function doesn't return anything, it prints the result to console.
    """
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'title': pr_title,
        'head': head_branch,
        'base': base_branch,
        'body': pr_body
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Pull Request created successfully: {response.json()['html_url']}")
    else:
        print(f"Error creating pull request: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    github_token = sys.argv[1]
    base_branch = sys.argv[2]
    head_branch = sys.argv[3]
    pr_title = sys.argv[4]
    pr_body = sys.argv[5] if len(sys.argv) > 5 else ''

    # Replace with your GitHub username/repo
    owner = 'your-github-username'
    repo = 'your-repository-name'

    create_pull_request(github_token, owner, repo, base_branch, head_branch, pr_title, pr_body)
