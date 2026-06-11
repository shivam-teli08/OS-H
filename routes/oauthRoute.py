import os

import requests
from flask import Blueprint, request, render_template
from redisConnection import redisConnection
from services.oAuthUrl import login as github_login_redirect

oauthRoute_bp = Blueprint("oauthRoute", __name__)


@oauthRoute_bp.route("/login")
def login():
    return render_template("oAuth.html")


@oauthRoute_bp.route("/oAuth")
def oAuth():
    return github_login_redirect()


@oauthRoute_bp.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if not code or not state:
        return {"error": "Missing OAuth code or state"}, 400

    r = redisConnection()
    stored = r.get(f"oauth_state:{state}")
    if not stored:
        return {"error": "Invalid OAuth state"}, 403

    r.delete(f"oauth_state:{state}")

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    if not client_id or not client_secret:
        return {"error": "Missing GitHub OAuth client configuration"}, 500

    token_payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    redirect_uri = os.getenv("GITHUB_REDIRECT_URI")
    if redirect_uri:
        token_payload["redirect_uri"] = redirect_uri

    token_res = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data=token_payload,
        timeout=10,
    )
    if not token_res.ok:
        return {"error": "Failed to exchange GitHub OAuth code"}, token_res.status_code

    token_data = token_res.json()
    access_token = token_data.get("access_token")
    if not access_token:
        return {
            "error": token_data.get("error_description", "GitHub did not return an access token")
        }, 400

    user_res = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=10,
    )
    if not user_res.ok:
        return {"error": "Failed to fetch GitHub user"}, user_res.status_code

    user = user_res.json()

    return {
        "github_id": user.get("id"),
        "username": user.get("login"),
        "avatar": user.get("avatar_url"),
    }
