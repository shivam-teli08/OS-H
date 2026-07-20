from schemas.issues import Issue
def get_paginated_issues(cursor, limit):
    query = Issue.query.order_by(Issue.id.asc())
    if cursor:
        query = query.filter(Issue.id > cursor)
    return query.limit(limit).all()