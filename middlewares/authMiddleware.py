from functools import wraps 
from flask import redirect,url_for,session


def login_check(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not session.get("github_id")or not session.get("username"):
            return redirect(url_for("oauthRoute.login"))
        return func(*args,**kwargs)
    return wrapper
