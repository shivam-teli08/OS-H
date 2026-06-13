from datetime import datetime

from sqlalchemy.dialects.postgresql import ARRAY

from extensions import db

class Intrests(db.Model):
    __tablename__='user_intrests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    languages = db.Column(ARRAY(db.String), default=[])
    skill_level = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(100), nullable=False)
    interests = db.Column(ARRAY(db.String), default=[])
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
