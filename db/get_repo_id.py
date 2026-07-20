from extensions import db
from schemas.repository import Repository
from schemas.issue import Issue
def get_repo_id_by_repoName_and_owner(repo_name, owner):
    """
    Fetches the repository ID based on the repository name and owner.
    Args:
        repo_name (str): The name of the repository.
        owner (str): The owner of the repository.   
    """
    repo = Repository.query.filter_by(name=repo_name, owner=owner).first()
    if repo:
        return repo.id
    else:
        return None