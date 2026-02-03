import json
from pathlib import Path
from config import DATA_DIR, PROCESSED_FILE

Path(DATA_DIR).mkdir(exist_ok=True)

def save_processed_lead(lead: dict):
    file_path = Path(PROCESSED_FILE)
    if file_path.exists():
        data = json.loads(file_path.read_text(encoding="utf-8"))
    else:
        data = []

    data.append(lead)
    file_path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
