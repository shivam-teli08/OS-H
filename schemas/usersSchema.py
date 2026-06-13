from datetime import datetime

from extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    github_id = db.Column(db.BigInteger, unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    avatar_url = db.Column(db.Text)
    email = db.Column(db.String(255))
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
