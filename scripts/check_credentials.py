import json
from pathlib import Path

creds_file = Path("/config/application_default_credentials.json")
if not creds_file.is_file():
    raise Exception('gcloud application_default_credentials.json file missing')

with creds_file.open() as f:
    data = json.load(f)

logged_in_project = data.get("quota_project_id")
if not logged_in_project == "paul-personal-306310":
    raise Exception(f"gcloud is logged into {logged_in_project}. Please log into paul-personal-306310 instead")
