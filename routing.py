def assign_lead(score, branch_manager, worker_code):
    if score >= 70:
        return "HOT", branch_manager
    elif score >= 40:
        return "WARM", worker_code
    else:
        return "COLD", "GeneralPool"
