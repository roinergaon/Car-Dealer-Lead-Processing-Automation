from models import LeadInput
from config import DISPOSABLE_DOMAINS

def validate_lead(lead: LeadInput):
    if not lead.BranchID.isdigit():
        return False, "BranchID must be numeric"

    if not lead.Email and not lead.Phone:
        return False, "Invalid email + no phone"

    if lead.Phone:
        if not lead.Phone.isdigit() or len(lead.Phone) != 10 or not lead.Phone.startswith("05"):
            return False, "Invalid Israeli phone number"

    if not lead.FirstName or not lead.LastName:
        return False, "Missing name"

    if lead.Email:
        email_parts = lead.Email.split("@")
        if len(email_parts) != 2 or "." not in email_parts[1]:
            return False, "Invalid email format"
        domain = email_parts[1].lower()
        if domain in DISPOSABLE_DOMAINS:
            return False, "Disposable email not allowed"

    return True, ""
