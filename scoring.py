def calculate_score(car, enrichment):
    score = 0
    if enrichment:
        if enrichment.get("lead_priority") == "High":
            score += 40
        elif enrichment.get("lead_priority") == "Medium":
            score += 20
        if enrichment.get("email_insights", {}).get("trust_level") == "High":
            score += 20
        if enrichment.get("phone_insights", {}).get("verified"):
            score += 20
    if car:
        if car.get("category") == "Luxury":
            score += 20
        elif car.get("category") == "Electric":
            score += 15
        if car.get("availability") == "In Stock":
            score += 10
    return min(score, 100)
