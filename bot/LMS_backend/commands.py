import os
import requests
from dotenv import load_dotenv

def env_path(levels_up=3, filename=".env.docker.secret"):
    path = __file__
    for _ in range(levels_up):
        path = os.path.dirname(path)
    return os.path.join(path, filename)

load_dotenv(env_path())
print(env_path())

LMS_API_BASE_URL = os.getenv("LMS_API_BASE_URL", "http://localhost:42002")
LMS_API_KEY = os.getenv("LMS_API_KEY", "")

HEADERS = {"Authorization": f"Bearer {LMS_API_KEY}"}

def get_items():
    try:
        resp = requests.get(f"{LMS_API_BASE_URL}/items/", headers=HEADERS, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def get_pass_rates(lab_id: str):
    """Fetch per-task pass rates for a lab"""
    try:
        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/pass-rates",
            params={"lab": lab_id},
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def check_health():
    """Check backend health via /items/"""
    try:
        items = get_items()
        if isinstance(items, str):  # error returned
            return items
        return f"Backend is healthy. {len(items)} items available."
    except Exception as e:
        return f"Backend error: {e}"