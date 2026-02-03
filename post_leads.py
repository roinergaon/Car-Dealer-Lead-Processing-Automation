import json
import os
import requests

if os.getenv("RUN_IN_DOCKER") == "1":
    API_URL = "http://main-api:8000/api/leads"
else:
    API_URL = "http://127.0.0.1:8000/api/leads"

SAMPLE_FILE = "data/sample_leads.json"

# Load the sample file
with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract only the 'leads' list (the API expects a list, not the whole JSON with description)
leads_list = data.get("leads", [])

if not leads_list:
    print("No leads found in the file")
else:
    print(f"Sending {len(leads_list)} lead(s) to the API...")

    # Send POST request to the API
    resp = requests.post(API_URL, json=leads_list)

    # Print status code and the API response
    print("Status:", resp.status_code)
    print("Response:", resp.json())
    pass





