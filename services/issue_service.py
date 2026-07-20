from db.get_paginated_issues import get_paginated_issues
def fetch_paginated_issues(cursor, limit):
    return get_paginated_issues(cursor, limit)