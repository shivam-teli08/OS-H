from schemas.usersSchema import User
from schemas.intrestInfoSchema import Intrests 
from flask import session
from extensions import db

def CheckUserExists(userJsonSchema):
    user = User.query.filter_by(
        github_id=userJsonSchema["id"]
    ).first()
    if not user:
        user = User(
            github_id=userJsonSchema["id"],
            username=userJsonSchema["login"],
            avatar_url=userJsonSchema.get("avatar_url"),
            email=userJsonSchema.get("email")
        )
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id  
        return user, True
    session["user_id"] = user.id
    return user, False

def save_onboarding(form_data):
    experience_level = form_data.get("experience_level", form_data.get("skill_level", "beginner"))
    goal = form_data.get("goal", "first_contribution")
    languages = form_data.getlist("languages") or []
    frameworks = form_data.getlist("frameworks") or []
    interests = form_data.getlist("interests") or []
    weekly_availability = form_data.get("weekly_availability", "1-3 hrs/week")
    user_id = session["user_id"]
    profile = Intrests(
        user_id=user_id,
        skill_level=experience_level,
        goal=goal,
        languages=languages,
        frameworks=frameworks,
        interests=interests,
        weekly_availability=weekly_availability,
    )
    db.session.add(profile)
    db.session.commit()
    return profile
