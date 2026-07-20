from extensions import db
from schemas.issue import Issue

def save_issue(issue,repo_id):
    for issue in issues:
            if "pull_request" in issue:
                continue
            existing_issue = Issue.query.filter_by(
                github_issue_id=issue["id"]
            ).first()
            if existing_issue:
                continue
            db.session.add(
                Issue(
                    github_issue_id=issue["id"],
                    repository_id=repo_id,   
                    title=issue["title"],
                    body=issue["body"],
                    state=issue["state"],
                    labels=issue["labels"],
                    author=issue["user"]["login"],
                    created_at=datetime.fromisoformat(
                        issue["created_at"].replace("Z", "+00:00")
                    ),
                    updated_at=datetime.fromisoformat(
                        issue["updated_at"].replace("Z", "+00:00")
                    ),
                    closed_at=(
                        datetime.fromisoformat(
                            issue["closed_at"].replace("Z", "+00:00")
                        )
                        if issue["closed_at"] else None
                    ),
                    html_url=issue["html_url"],
                    last_synced_at=datetime.utcnow()
                )
            )
    db.session.commit()
    print("Issues saved successfully.")