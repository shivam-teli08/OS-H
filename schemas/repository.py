from extensions import db
from datetime import datetime
class Repository(db.Model):
    __tablename__ = 'repositories'
    id = db.Column(db.Integer,primary_key=True)
    github_id = db.Column(db.Integer,unique=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    owner= db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=True)
    language = db.Column(db.String(50),nullable=True)
    stars = db.Column(db.Integer,nullable=False,default=0)
    forks = db.Column(db.Integer,nullable=False,default=0)
    open_issues_count = db.Column(db.Integer,nullable=False,default=0)
    html_url = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)
    last_synced_at= db.Column(db.DateTime,nullable=False)