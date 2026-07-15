from requests import get
from github.client import headers
def search_repository(language):
    url = (
    f"https://api.github.com/search/repositories"
    f"?q=language:{language}"
    f"&sort=stars"
    f"&order=desc"
    f"&per_page=100"
)
    response = get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        return None
