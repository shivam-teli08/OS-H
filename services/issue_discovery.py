from db.repoCaller import get_all_repo
from schemas.issue import Issue
from github.client import headers
import requests
from extensions import db
from datetime import datetime

def discover_issues():
    repos = get_all_repo()
    if not repos:
        print("No repositories found.")
        return
    for repo in repos:
        print(f"{repo.name} This repo going to processed")
        url = f"https://api.github.com/repos/{repo.owner}/{repo.name}/issues"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch issues for {repo.owner}/{repo.name}")
            continue
        data = response.json()
        print(f"{data} we received for {repo.n}")
        save_issues(data,repo.id)