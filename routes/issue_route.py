from flask import Blueprint,request,jsonify
from service.issue_service import fetch_paginated_issues

issue_bp = Blueprint("issues",__name__)
@issue_bp.route("/",methods=["GET"])
def get_issues():
    cursor=request.args.get("cursor",type=int)
    limit=request.args.get("limit",default=20,type=int)
    issues = fetch_paginated_issues(cursor,limit)
    if not issues:
        return jsonify({
            "has_next": False,
            "next_cursor": None,
            "issues": []
        })
    next_cursor = issues[-1].id
    return jsonify({
        "has_next": True,
        "next_cursor": next_cursor,
        "issues": [
            {
                "id": issue.id,
                "github_issue_id": issue.github_issue_id,
                "title": issue.title,
                "body": issue.body,
                "state": issue.state,
                "labels": issue.labels,
                "author": issue.author,
                "html_url": issue.html_url,
                "created_at": issue.created_at.isoformat(),
                "updated_at": issue.updated_at.isoformat()
            }
            for issue in issues
        ]
    })