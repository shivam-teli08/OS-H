LABELS = [
    "good first issue",
    "help wanted"
]
LANGUAGES = [
    "Python",
    "Java",
    "JavaScript",
    "Go",
    "Rust",
    "TypeScript"
]
query = 'is:issue is:open label:"good first issue"'

url = "https://api.github.com/search/issues"
params ={
    "q": 'is:issue is:open label:"good first issue"',
        "sort": "updated",
        "order": "desc",
        "per_page": 10
}