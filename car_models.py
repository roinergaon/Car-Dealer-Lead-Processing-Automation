from pathlib import Path
from config import CAR_FILE
from logger import log_stage

def parse_car_entry(entry: str) -> dict:
    def extract(field):
        for line in entry.splitlines():
            if line.startswith(field + ":"):
                return line.split(":", 1)[1].strip()
        return None

    return {
        "model_name": extract("Model"),
        "category": extract("Category"),
        "price_range": extract("Price Range"),
        "availability": extract("Availability")
    }

def load_car_models():
    CAR_MODELS = {}
    file_path = Path(CAR_FILE)
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
        entries = content.split("--------------------------------------------------------------------------------")
        for entry in entries:
            if "Model ID:" in entry:
                for line in entry.splitlines():
                    if line.startswith("Model ID:"):
                        model_id = line.split(":", 1)[1].strip()
                        CAR_MODELS[model_id] = parse_car_entry(entry)
                        break
    else:
        log_stage("file_error", {}, reason="car_models.txt not found")
    return CAR_MODELS
