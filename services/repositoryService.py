import requests
from github.client import headers
from schemas.issue import Issue
from schemas.repositary import Repository


def getRepositories():
    try:
        response = requests.get(
            "https://api.github.com/search/repositories",
            headers=headers,
            params={
                "q": "is:public language:Python",
                "sort": "stars",
                "order": "desc",
                "per_page": 10,
            },
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()
        return payload.get("items", [])
    except Exception:
        return []


def get_repo_issues(repo_full_name, per_page=10):
    try:
        response = requests.get(
            "https://api.github.com/search/issues",
            headers=headers,
            params={
                "q": f"repo:{repo_full_name} is:issue is:open",
                "sort": "updated",
                "order": "desc",
                "per_page": per_page,
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def get_paginated_repositories(page=1, per_page=5):
    page = max(1, int(page or 1))
    per_page = max(1, min(int(per_page or 5), 20))
    pagination = Repository.query.order_by(Repository.stars.desc(), Repository.id.desc())
    page_obj = pagination.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "items": [
            {
                "id": repo.id,
                "full_name": repo.full_name,
                "name": repo.name,
                "description": repo.description or "No description available yet.",
                "language": repo.language or "Unknown",
                "stars": repo.stars,
                "forks": repo.forks,
                "open_issues": repo.open_issues,
                "repo_url": repo.repo_url,
            }
            for repo in page_obj.items
        ],
        "pagination": {
            "page": page_obj.page,
            "pages": page_obj.pages,
            "per_page": page_obj.per_page,
            "total": page_obj.total,
            "has_prev": page_obj.has_prev,
            "has_next": page_obj.has_next,
        },
    }


def get_paginated_issues(page=1, per_page=5):
    page = max(1, int(page or 1))
    per_page = max(1, min(int(per_page or 5), 20))
    pagination = Issue.query.order_by(Issue.created_at.desc().nullslast(), Issue.id.desc())
    page_obj = pagination.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "items": [
            {
                "id": issue.id,
                "title": issue.title,
                "state": issue.state,
                "author": issue.author,
                "comments": issue.comments,
                "difficulty": issue.difficulty or "Beginner",
                "issue_url": issue.issue_url,
                "repository_name": issue.repository.full_name if issue.repository else "Unknown",
            }
            for issue in page_obj.items
        ],
        "pagination": {
            "page": page_obj.page,
            "pages": page_obj.pages,
            "per_page": page_obj.per_page,
            "total": page_obj.total,
            "has_prev": page_obj.has_prev,
            "has_next": page_obj.has_next,
        },
    }