import logging
import json
from pathlib import Path

# -------------------------
# Setup structured logger
# -------------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "leads.log"

logger = logging.getLogger("lead_pipeline")
logger.setLevel(logging.INFO)

# Console handler
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(ch)

# File handler
fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
fh.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(fh)


def log_stage(stage, lead_data, score=None, priority=None, assigned_to=None, reason=None, **kwargs):
    """
    Logs each stage of the lead processing pipeline in structured JSON format.
    Saves logs both to console and to file.
    """
    log_entry = {
        "stage": stage,
        "original_lead": lead_data,
        "score": score,
        "priority": priority,
        "assigned_to": assigned_to,
        "reason": reason
    }
    log_entry.update(kwargs)

    pretty_json = json.dumps(log_entry, ensure_ascii=False, indent=2)
    logger.info(pretty_json)

