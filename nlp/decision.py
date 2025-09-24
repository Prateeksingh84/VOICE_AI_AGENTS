def screening_score(skill_match, years, notice_days, willingness_score, tone):
    exp_score = min(years / 5.0, 1.0)
    availability = 1.0 if notice_days <= 14 else (0.7 if notice_days <= 30 else 0.4)
    score = (skill_match*0.4 + exp_score*0.2 + availability*0.15 +
             willingness_score*0.15 + tone*0.1)
    return round(score * 100)

def summarize_decision(score: int) -> str:
    if score >= 70:
        return "Advance to Technical Interview"
    elif score >= 50:
        return "Escalate to HR Review"
    else:
        return "Reject - Not suitable"
