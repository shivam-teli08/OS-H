from flask import Blueprint, jsonify
from services.repositoryService import getRepositories

repository_bp = Blueprint("repository", __name__)

@repository_bp.route("/repositories/sync", methods=["GET"])
def sync_repositories():
    try:
        result = getRepositories()

        return jsonify({
            "success": True,
            "message": "Repositories fetched successfully",
            "data": result
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500