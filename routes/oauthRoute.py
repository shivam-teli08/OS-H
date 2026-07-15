import os
import requests
from flask import Blueprint, request, render_template,session,redirect
from redisConnection import redisConnection
from services.oAuthUrl import login as github_login_redirect
from db.dboperations import CheckUserExists
oauthRoute_bp = Blueprint("oauthRoute", __name__)


@oauthRoute_bp.route("/login")
def login():
    if session.get("github_id") and session.get("username"):
        return redirect("/dashboard")
    return render_template("oAuth.html")


@oauthRoute_bp.route("/oAuth")
def oAuth():
    return github_login_redirect()


@oauthRoute_bp.route("/callback")
def callback():
    try:
        code = request.args.get("code")
        state = request.args.get("state")

        if not code or not state:
            return {"error": "Missing OAuth code or state"}, 400

        r = redisConnection()
        stored = r.get(f"oauth_state:{state}")
        if not stored:
            return {"error": "Invalid OAuth state"}, 403

        r.delete(f"oauth_state:{state}")

        token_res = requests.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": os.getenv("CLIENT_ID"),
                "client_secret": os.getenv("CLIENT_SECRET"),
                "code": code,
            },
        )

        access_token = token_res.json().get("access_token")
        
        user_res = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"},
        )

        user = user_res.json()

        session["github_id"] = user.get("id")
        session["username"] = user.get("login")
        session["avatar"] = user.get("avatar_url")

        user, is_new = CheckUserExists(user)

        return redirect("/onboarding" if is_new else "/dashboard")

    except Exception as e:
        print("❌ CALLBACK ERROR:", str(e))
        return {"error": str(e)}, 500
