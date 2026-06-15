from flask import Blueprint, redirect, render_template, request, url_for

from db.getProfileinfo import getProfileinfo
from extensions import db
from middlewares.authMiddleware import login_check

dashBoardRoutebp = Blueprint("dashBoardRoute", __name__)


@dashBoardRoutebp.route("/dashboard")
@login_check
def dashboard():
    return render_template("dashboard.html")


@dashBoardRoutebp.route("/profile")
@login_check
def profile():
    userInfo = getProfileinfo()
    if not userInfo:
        return redirect(url_for("oauthRoute.login"))

    return render_template("profile.html", user=userInfo)


@dashBoardRoutebp.route("/edit-profile", methods=["GET", "POST"])
@login_check
def editProfile():
    userInfo = getProfileinfo()
    if not userInfo:
        return redirect(url_for("oauthRoute.login"))

    if request.method == "POST":
        userInfo.email = request.form.get("email", userInfo.email)
        userInfo.bio = request.form.get("bio", userInfo.bio)
        userInfo.location = request.form.get("location", userInfo.location)
        userInfo.company = request.form.get("company", userInfo.company)
        userInfo.college = request.form.get("college", userInfo.college)
        db.session.commit()
        return redirect(url_for("dashBoardRoute.profile"))

    profile_fields = ("email", "bio", "location", "company", "college")
    missing_fields = [
        field for field in profile_fields
        if not getattr(userInfo, field, None)
    ]

    return render_template(
        "edit_profile.html",
        user=userInfo,
        missing_fields=missing_fields,
    )
