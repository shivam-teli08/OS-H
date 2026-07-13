from dotenv import load_dotenv
import requests 
import os 

load_dotenv()

token=os.getenv("GITHUB_API_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}