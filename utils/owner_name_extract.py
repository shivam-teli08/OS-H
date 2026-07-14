import requests
from github.client import headers

def owner_name_extracter(data):
    repositories = []
    visited = set()
    for issue in data["data"]["items"]:
        repo_url = issue["repository_url"]
        if repo_url in visited:
            continue
        visited.add(repo_url)
        parts = repo_url.split("/")
        owner_name = parts[-2]
        repo_name = parts[-1]
        url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
        response = requests.get(
            url,
            headers=headers
        )
        if response.status_code == 200:
            repositories.append(response.json())
    return repositories