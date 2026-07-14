from flask import Blueprint, jsonify, redirect, url_for
from db.insertIssueOp import insert_issues
from db.insertRepoOp import insert_repository
from services.repositoryService import getRepositories, get_repo_issues

repository_bp = Blueprint("repository", __name__)


@repository_bp.route("/repositories/sync", methods=["GET"])
def sync_repositories():
    try:
        result = getRepositories()
        for repo_data in result:
            repo = insert_repository(repo_data)
            issue_payload = get_repo_issues(repo.full_name)
            if issue_payload:
                insert_issues(issue_payload, repo)

        return redirect(url_for("dashBoardRoute.dashboard"))

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500