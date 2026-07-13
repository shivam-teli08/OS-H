from extensions import db

class Repository(db.Model):
    __tablename__ = "repositories"
    id = db.Column(db.Integer,primary_key=True)
    github_repo_id = db.Column(db.BigInteger,unique=True,nullable=False)
    owner=db.Column(db.String(255),nullable=False)
    name=db.Column(db.String(255),nullable=False)
    full_name=db.Column(db.String(255),unique=True,nullable=False)
    description=db.Column(db.Text)
    language=db.Column(db.String(100))
    stars=db.Column(db.Integer,default=0)
    forks = db.Column(db.Integer, default=0)
    open_issues = db.Column(db.Integer, default=0)
    topics = db.Column(db.JSON)
    license = db.Column(db.String(100))
    default_branch = db.Column(db.String(100))
    last_commit_at = db.Column(db.DateTime)
    repo_url = db.Column(db.String(500))
    is_archived = db.Column(db.Boolean, default=False)
    last_synced_at = db.Column(db.DateTime)