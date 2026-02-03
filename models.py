from pydantic import BaseModel

class LeadInput(BaseModel):
    BranchID: str
    WorkerCode: str
    AskedCar: str
    FirstName: str
    LastName: str
    Email: str
    Phone: str
    FromWebSite: str
    Area: str
