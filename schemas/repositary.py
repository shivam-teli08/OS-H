from extensions import db

class Repository(db.Model):
    __tablename__ = "repositories"
    id = db.Column(db.Integer, primary_key=True)
    github_repo_id = db.Column(db.BigInteger, unique=True, nullable=False, index=True)
    owner = db.Column(db.String(255), nullable=False)
    owner_avatar = db.Column(db.String(500))
    name = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text)
    language = db.Column(db.String(100), index=True)
    stars = db.Column(db.Integer, default=0, index=True)
    forks = db.Column(db.Integer, default=0)
    open_issues = db.Column(db.Integer, default=0)
    topics = db.Column(db.JSON)
    license = db.Column(db.String(100))
    default_branch = db.Column(db.String(100))
    homepage = db.Column(db.String(500))
    repo_url = db.Column(db.String(500))
    is_archived = db.Column(db.Boolean, default=False)
    last_commit_at = db.Column(db.DateTime)
    last_synced_at = db.Column(db.DateTime)
    issues = db.relationship(
        "Issue",
        back_populates="repository",
        lazy=True,
        cascade="all, delete-orphan"
    )