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
    <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"400\" height=\"200\">
        <defs>
            <style>
                .background {{ fill: #1e1e2e; }}
                .title {{ fill: #ffffff; font-size: 24px; font-family: Arial, sans-serif; font-weight: bold; }}
                .stat {{ fill: #a6e22e; font-size: 18px; font-family: 'Courier New', monospace; animation: fadeIn 2s ease-in-out; }}
                .label {{ fill: #66d9ef; font-size: 18px; font-family: 'Courier New', monospace; }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                @keyframes bounce {{
                    0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                    40% {{ transform: translateY(-10px); }}
                    60% {{ transform: translateY(-5px); }}
                }}
                .animated {{ animation: bounce 2s infinite; }}
            </style>
        </defs>
        <rect width=\"400\" height=\"200\" class=\"background\"/>
        <text x=\"10\" y=\"30\" class=\"title animated\">GitHub Stats</text>
        <text x=\"10\" y=\"70\" class=\"label\">⭐ Stars:</text>
        <text x=\"150\" y=\"70\" class=\"stat\">{{stats['stars']}}</text>
        <text x=\"10\" y=\"100\" class=\"label\">👥 Followers:</text>
        <text x=\"150\" y=\"100\" class=\"stat\">{{stats['followers']}}</text>
        <text x=\"10\" y=\"130\" class=\"label\">🔗 Following:</text>
        <text x=\"150\" y=\"130\" class=\"stat\">{{stats['following']}}</text>
        <text x=\"10\" y=\"160\" class=\"label\">📦 Public Repos:</text>
        <text x=\"150\" y=\"160\" class=\"stat\">{{stats['repos']}}</text>
    </svg>
    """
    os.makedirs("generated", exist_ok=True)
    with open("generated/github_stats.svg", "w") as f:
        f.write(content)

if __name__ == "__main__":
    stats = fetch_github_stats()
    generate_svg(stats)
