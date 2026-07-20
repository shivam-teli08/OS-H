from extensions import db
from datetime import datetime
class Issue(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer,primary_key=True)
    github_issue_id=db.Column(db.BigInteger,nullable=False,unique=True,index=True)
    repository_id=db.Column(db.Integer,db.ForeignKey('repositories.id'),nullable=False,index=True)
    title=db.Column(db.String(255),nullable=False)
    body=db.Column(db.Text,nullable=True)
    state=db.Column(db.String(50),nullable=False)
    labels=db.Column(db.JSON,nullable=True)
    author=db.Column(db.String(255),nullable=False)
    created_at=db.Column(db.DateTime,nullable=False)
    updated_at=db.Column(db.DateTime,nullable=False)
    closed_at=db.Column(db.DateTime,nullable=True)
    html_url=db.Column(db.String(255),nullable=False)
    last_synced_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
