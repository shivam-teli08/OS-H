from schemas.repository import Repository
from extensions import db
from datetime import datetime


def save_repositories(repositories):
    for repo in repositories:
        existing_repo = Repository.query.filter_by(
            github_id=repo["id"]
        ).first()
        if existing_repo:
            continue  # Skip if the repository already exists
        repository_data = {
            "name": repo["name"],
            "owner": repo["owner"]["login"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "open_issues_count": repo["open_issues_count"],
            "html_url": repo["html_url"],
            "created_at": datetime.fromisoformat(
                repo["created_at"].replace("Z", "+00:00")
            ),
            "updated_at": datetime.fromisoformat(
                repo["updated_at"].replace("Z", "+00:00")
            ),
            "last_synced_at": datetime.utcnow(),
        }

        db.session.add(
            Repository(
                github_id=repo["id"],
                **repository_data
            )
        )
    db.session.commit()