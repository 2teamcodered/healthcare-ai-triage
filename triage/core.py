URGENT={"chest_pain","severe_breathing_difficulty","uncontrolled_bleeding"}
def triage(symptoms: set[str]) -> dict:
    urgent=sorted(symptoms & URGENT)
    return {"category":"urgent_review" if urgent else "routine_review", "matched_red_flags":urgent, "disclaimer":"Not a diagnosis; seek professional care."}
