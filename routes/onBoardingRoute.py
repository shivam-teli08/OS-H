from flask import Blueprint, redirect, render_template, request

from db.dboperations import save_onboarding as save_onboarding_data

onBoardingRoutebp=Blueprint("onBoardingRoute", __name__)

@onBoardingRoutebp.route("/onboarding")
def onboarding():
    return render_template("onboard.html")

@onBoardingRoutebp.route("/save-onboarding",methods=["POST"])
def save_onboarding():
    form_data = request.form
    save_onboarding_data(form_data)
    return redirect ("/dashboard")
