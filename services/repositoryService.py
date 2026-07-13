from pre_need_data.language_label import LABELS, LANGUAGES, query , url, params
import requests
from github.client import headers

def getRepositories():    
    response = requests.get(
        url,
        headers=headers,
        params=params
    )
    print(response.status_code)
    print(response.json())
    return "IT WORKS"