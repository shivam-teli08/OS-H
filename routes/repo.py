from flask import Blueprint
from schemas.repository import Repository
from services.repository_discovery import search_repository
from db.save_repositories import save_repositories
from services.issue_discovery import discover_issues
repo_bp = Blueprint("repo", __name__)

TARGET_REPOS_PER_LANGUAGE = 100

LANGUAGES = [
    "Python",
    "JavaScript",
    "TypeScript",
    "Java",
    "Go",
    "Rust",
]
@repo_bp.route("/search", methods=["POST"])
def search_repositories():
    for language in LANGUAGES:
        repo_count = Repository.query.filter_by(language=language).count()
        if repo_count < TARGET_REPOS_PER_LANGUAGE:
            need = TARGET_REPOS_PER_LANGUAGE - repo_count
            print(f"{language}: Need {need} repositories.")
            repos = search_repository(language)
            save_repositories(repos)
        else:
            print(f"{language}: Already has {repo_count} repositories. Skipping.")
    return {
        "message": "Repository discovery completed."
    }, 200

@repo_bp.route("/issues", methods=["GET"])
def discover_isss():
    result = discover_issues()
    return result if result else {"message": "No issues found or failed to fetch issues."}, 200