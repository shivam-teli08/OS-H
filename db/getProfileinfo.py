from flask import session
from schemas.usersSchema import User
from middlewares.authMiddleware import login_check
@login_check
def getProfileinfo():
    user_id = session["user_id"]
    print(f"user id is {user_id}")
    userInfo = User.query.filter_by(id=user_id).first()
    if not userInfo:
        return None
    return userInfo