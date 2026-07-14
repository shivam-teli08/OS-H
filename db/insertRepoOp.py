from schemas.repository import Repository
from extensions import db 

def insert_repository(repo_data):
    repository = Repository.query.filter_by(
        github_repo_id= repo_data["id"]
    ).first()
    if repositoy:
        return repository
    repository = Repository(
        github_repo_id=repo_data["id"],
        owner=repo_data["owner"]["login"],
        name=repo_data["name"],
        full_name=repo_data["full_name"],
        description=repo_data["description"],
        language=repo_data["language"],
        stars=repo_data["stargazers_count"],
        forks=repo_data["forks_count"],
        open_issues=repo_data["open_issues_count"],
        topics=repo_data["topics"],
        license=repo_data["license"]["spdx_id"] if repo_data["license"] else None,
        default_branch=repo_data["default_branch"],
        last_commit_at=None,          
        repo_url=repo_data["html_url"],
        is_archived=repo_data["archived"],
        last_synced_at=datetime.utcnow()
    )
    db.session.add(repository)
    db.session.commit()
    return repository