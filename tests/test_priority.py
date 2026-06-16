from app.services.priority_service import adjust_priority

def test_critical_priority():
    text = """
    Production outage affecting all users
    """
    result = adjust_priority(text, "High")
    assert result == "Critical"