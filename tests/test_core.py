from triage.core import triage
def test_red_flag(): assert triage({"chest_pain"})["category"] == "urgent_review"
