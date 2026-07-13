from extensions import db
class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True)
    github_issue_id = db.Column(db.BigInteger, unique=True, nullable=False)
    repository_id = db.Column(
        db.Integer,
        db.ForeignKey("repositories.id"),
        nullable=False
    )
    issue_number = db.Column(db.Integer)
    title = db.Column(db.String(500))
    body = db.Column(db.Text)
    state = db.Column(db.String(50))
    labels = db.Column(db.JSON)
    author = db.Column(db.String(255))
    comments = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    closed_at = db.Column(db.DateTime)
    issue_url = db.Column(db.String(500))
    difficulty = db.Column(db.String(50))
    last_synced_at = db.Column(db.DateTime)