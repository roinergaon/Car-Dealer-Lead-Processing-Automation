import httpx
from config import MOCK_API_URL
from logger import log_stage

async def enrich_lead_async(lead):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            res = await client.post(
                f"{MOCK_API_URL}/api/enrich",
                json={"email": lead.Email, "phone": lead.Phone, "area": lead.Area}
            )
            res.raise_for_status()
            return res.json().get("data")
    except Exception as e:
        log_stage("enrichment_failed", lead.model_dump(), reason=str(e))
        return None
