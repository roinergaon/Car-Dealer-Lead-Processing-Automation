from models import LeadInput
from config import DISPOSABLE_DOMAINS

def validate_lead(lead: LeadInput):
    """
       Validates the lead data including email and phone.

       # -----------------------------------------------
       # Email verification interface
       # -----------------------------------------------
       # Why email verification services are important for business automation:
       # 1. Ensures the email is deliverable, reducing bounce rates in campaigns.
       # 2. Prevents fake or disposable emails from entering the system, improving lead quality.
       # 3. Automates the process of filtering invalid leads, saving manual work.
       # 4. Increases trust and reliability of CRM and marketing analytics.

       # Example 3rd party API providers for email validation:

       # - ZeroBounce (https://www.zerobounce.net)
       # - Hunter.io (https://hunter.io/email-verifier)

       # Business benefits:
       # - Higher lead conversion rate due to accurate contacts.
       # - Reduced cost for marketing campaigns (emails only sent to valid addresses).
       # - Improved CRM data quality for analytics and reporting.
       # - Better reputation with email service providers (avoiding spam/bounce flag
   """

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
