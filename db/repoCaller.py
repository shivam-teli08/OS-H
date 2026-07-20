from extensions import db
from schemas.repository import Repository
def get_all_repo():
    """
    Fetches all repositories from the database.
    Returns:
        List of Repository objects.
    """
    return Repository.query.all()
