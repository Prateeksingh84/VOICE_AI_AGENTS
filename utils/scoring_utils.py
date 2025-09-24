def screening_score(skill_match, years, notice_days, willingness_score, tone):
    """
    Compute candidate screening score.
    
    Parameters:
    - skill_match: float (0 to 1) representing how well skills match
    - years: int, years of experience
    - notice_days: int, notice period in days
    - willingness_score: float (0 to 1)
    - tone: float (0 to 1)
    
    Returns:
    - score (0-100)
    """
    exp_score = min(years / 5.0, 1.0)
    availability = 1.0 if notice_days <= 14 else (0.7 if notice_days <= 30 else 0.4)
    score = (
        skill_match * 0.4 +
        exp_score * 0.2 +
        availability * 0.15 +
        willingness_score * 0.15 +
        tone * 0.1
    )
    return round(score * 100)

def summarize_decision(score: int) -> str:
    """
    Convert numerical score into HR decision.
    """
    if score >= 70:
        return "Advance to Technical Interview"
    elif score >= 50:
        return "Escalate to HR Review"
    else:
        return "Reject - Not suitable"

# 🔹 Test code
if __name__ == "__main__":
    # Example candidate data
    skill_match = 0.8        # 80% skill match
    years = 3                 # 3 years experience
    notice_days = 14          # notice period
    willingness_score = 0.9   # very willing
    tone = 0.85               # good tone

    score = screening_score(skill_match, years, notice_days, willingness_score, tone)
    decision = summarize_decision(score)

    print(f"📊 Screening Score: {score}")
    print(f"✅ Decision: {decision}")
