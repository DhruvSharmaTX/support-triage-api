CRITICAL_KEYWORDS = [
    "outage",
    "production down",
    "security breach",
    "data leak",
    "tenant data",
    "all users",
    "critical",
]
def adjust_priority(text, current_priority):
    text = text.lower()
    for keyword in CRITICAL_KEYWORDS:
        if keyword in text:
            return "Critical"
    return current_priority
