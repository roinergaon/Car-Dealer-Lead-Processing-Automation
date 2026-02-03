from logger import log_stage
from storage import save_processed_lead
from validation import validate_lead
from enrichment import enrich_lead_async
from car_models import load_car_models
from branches import load_branches
from scoring import calculate_score
from routing import assign_lead

CAR_MODELS = load_car_models()
BRANCH_DATA = load_branches()

async def process_lead(lead):
    log_stage("received", lead.model_dump())

    valid, reason = validate_lead(lead)
    if not valid:
        log_stage("rejected", lead.model_dump(), reason=reason)
        save_processed_lead({
            "original_lead": lead.model_dump(),
            "status": "rejected",
            "reason": reason
        })
        return

    branch = BRANCH_DATA.get(lead.BranchID, BRANCH_DATA.get("400"))
    car = CAR_MODELS.get(lead.AskedCar)
    enrichment = await enrich_lead_async(lead)
    score = calculate_score(car, enrichment)
    priority, assigned_to = assign_lead(score, branch["manager"], lead.WorkerCode)

    final = {
        "original_lead": lead.model_dump(),
        "branch_info": {
            "branch_id": lead.BranchID,
            "name": branch["name"],
            "manager": branch["manager"],
            "region": branch["region"]
        },
        "car_info": {
            "model_id": lead.AskedCar,
            "model_name": car["model_name"] if car else None,
            "category": car["category"] if car else None,
            "price_range": car["price_range"] if car else None
        },
        "enrichment": {
            "geographic": enrichment.get("geographic") if enrichment else None,
            "email_insights": enrichment.get("email_insights") if enrichment else None,
            "phone_insights": enrichment.get("phone_insights") if enrichment else None,
            "lead_priority": enrichment.get("lead_priority") if enrichment else None
        },
        "score": score,
        "priority": priority,
        "assigned_to": assigned_to,
        "status": "processed"
    }

    log_stage("processed", lead.model_dump(), score=score, priority=priority)
    save_processed_lead(final)
    log_stage("done", lead.model_dump(), score=score, priority=priority, assigned_to=assigned_to)
