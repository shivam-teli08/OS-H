from redisConnection import redisConnection
import secrets
from flask import redirect
import os
from urllib.parse import urlencode

def login():
    client_id = os.getenv("CLIENT_ID")
    if not client_id:
        return "Missing CLIENT_ID in environment", 500
    r = redisConnection()
    state = secrets.token_urlsafe(32)
    r.set(f"oauth_state:{state}", "1", ex=600)
    params = {
        "client_id": client_id,
        "state": state,
        "scope": "read:user user:email",
    }
    # redirect_uri = os.getenv("GITHUB_REDIRECT_URI")
    # if redirect_uri:
    #     params["redirect_uri"] = redirect_uri

    url = f"https://github.com/login/oauth/authorize?{urlencode(params)}"
    return redirect(url)
