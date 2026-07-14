from extensions import db

class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True)
    github_issue_id = db.Column(db.BigInteger, unique=True, nullable=False, index=True)
    repository_id = db.Column(
        db.Integer,
        db.ForeignKey("repositories.id"),
        nullable=False,
        index=True
    )
    issue_number = db.Column(db.Integer)
    title = db.Column(db.String(500), nullable=False)
    body = db.Column(db.Text)
    state = db.Column(db.String(50), index=True)
    labels = db.Column(db.JSON)
    author = db.Column(db.String(255))
    assignee = db.Column(db.String(255))
    author_association = db.Column(db.String(50))
    comments = db.Column(db.Integer, default=0)
    experience_level = db.Column(db.String(20), index=True)
    # Beginner / Intermediate / Advanced
    issue_url = db.Column(db.String(500))
    created_at = db.Column(d
    b.DateTime)
    updated_at = db.Column(db.DateTime)
    closed_at = db.Column(db.DateTime)
    last_synced_at = db.Column(db.DateTime)