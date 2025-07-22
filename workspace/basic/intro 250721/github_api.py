# github_api.py
import requests

def get_github_user_info(username):
    """
    GitHub 사용자 정보를 반환하거나, 실패 시 None 반환
    """
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException:
        return None
