from fastapi import FastAPI, BackgroundTasks
from typing import List
from models import LeadInput
from processing import process_lead

app = FastAPI(title="Car Dealer Lead Processing API")

@app.post("/api/leads")
def receive_leads(leads: List[LeadInput], background_tasks: BackgroundTasks):
    for lead in leads:
        background_tasks.add_task(process_lead, lead)
    return {"message": f"{len(leads)} lead(s) received"}
