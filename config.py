import os

MOCK_API_URL = os.getenv("MOCK_API_URL", "http://mock-api:8001")

DISPOSABLE_DOMAINS = [
    "mailinator.com", "10minutemail.com", "dispostable.com",
    "tempmail.com", "yopmail.com"
]

DATA_DIR = "data"
PROCESSED_FILE = f"{DATA_DIR}/processed_leads.json"
BRANCH_FILE = f"{DATA_DIR}/branch_config.xlsx"
CAR_FILE = f"{DATA_DIR}/car_models.txt"
