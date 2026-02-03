import os
import pandas as pd
from logger import log_stage
from config import BRANCH_FILE

def load_branches():
    if os.path.exists(BRANCH_FILE):
        df = pd.read_excel(BRANCH_FILE)
        return {
            str(row["BranchID"]): {
                "name": row["Name"],
                "manager": row["Manager"],
                "region": row["Region"]
            }
            for _, row in df.iterrows()
        }
    else:
        log_stage("file_error", {}, reason="branch_config.xlsx not found")
        return {
            "400": {"name": "Tel Aviv Showroom", "manager": "David Cohen", "region": "Center"}
        }
