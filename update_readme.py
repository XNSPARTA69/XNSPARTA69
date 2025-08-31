import requests
import os

# GitHub API URL
API_URL = 'https://api.github.com/users/XNSPARTA69'

def fetch_github_stats():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return {
            "stars": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0),
            "repos": data.get("public_repos", 0)
        }
    else:
        return {}

def generate_svg(stats):
    content = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">
        <rect width="400" height="200" fill="#1e1e2e"/>
        <text x="10" y="30" fill="#ffffff" font-size="24">GitHub Stats</text>
        <text x="10" y="60" fill="#ffffff" font-size="18">Stars: {stats['stars']}</text>
        <text x="10" y="90" fill="#ffffff" font-size="18">Followers: {stats['followers']}</text>
        <text x="10" y="120" fill="#ffffff" font-size="18">Following: {stats['following']}</text>
        <text x="10" y="150" fill="#ffffff" font-size="18">Public Repos: {stats['repos']}</text>
    </svg>
    """
    os.makedirs("generated", exist_ok=True)
    with open("generated/github_stats.svg", "w") as f:
        f.write(content)

if __name__ == "__main__":
    stats = fetch_github_stats()
    generate_svg(stats)