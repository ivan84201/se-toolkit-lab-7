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
    
def get_learners():
    try:
        resp = requests.get(f"{LMS_API_BASE_URL}/learners/", headers=HEADERS, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def get_scores(lab_id: str):
    try:
        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/scores",
            params={"lab": lab_id},
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def get_timeline(lab_id: str):
    try:
        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/timeline",
            params={"lab": lab_id},
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def get_groups(lab_id: str):
    try:
        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/groups",
            params={"lab": lab_id},
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"
    
def get_top_learners(lab_id: str = None, limit: int = 5):
    try:
        params = {"limit": limit}
        if lab_id:
            params["lab"] = lab_id

        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/top-learners",
            params=params,
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"

def get_completion_rate(lab_id: str):
    try:
        resp = requests.get(
            f"{LMS_API_BASE_URL}/analytics/completion-rate",
            params={"lab": lab_id},
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return f"Backend error: {e}"


def trigger_sync():
    try:
        resp = requests.post(
            f"{LMS_API_BASE_URL}/pipeline/sync",
            headers=HEADERS,
            timeout=5
        )
        resp.raise_for_status()
        return {"status": "sync triggered"}
    except requests.RequestException as e:
        return f"Backend error: {e}"