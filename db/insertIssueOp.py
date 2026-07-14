from datetime import datetime
from models.issue import Issue
from extensions import db
def insert_issues(issue_data, repo):
    for issue in issue_data["data"]["items"]:
        if repo.stars < 1000:
            difficulty = "Beginner"
        elif repo.stars < 10000:
            difficulty = "Intermediate"
        else:
            difficulty = "Advanced"
        existing_issue = Issue.query.filter_by(
            github_issue_id=issue["id"]
        ).first()
        if existing_issue:
            continue
        new_issue = Issue(
            github_issue_id=issue["id"],
            repository_id=repo.id,
            issue_number=issue["number"],
            title=issue["title"],
            body=issue["body"],
            state=issue["state"],
            labels=[label["name"] for label in issue["labels"]],
            author=issue["user"]["login"],
            comments=issue["comments"],
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
                if issue["closed_at"]
                else None
            ),
            issue_url=issue["html_url"],
            difficulty=difficulty,
            last_synced_at=datetime.utcnow(),
        )
        db.session.add(new_issue)
    db.session.commit()