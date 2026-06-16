import json
from app.models.analysis_result import AnalysisResult

def save_analysis_result(db, title, description, analysis):
    record = AnalysisResult(
        title=title,
        description=description,
        predicted_category=analysis["predicted_category"],
        predicted_priority=analysis["predicted_priority"],
        confidence=analysis["confidence"],
        similar_ticket_id=analysis["similar_ticket"]["ticket_id"],
        recommended_articles=json.dumps(analysis["recommended_articles"]),
        reasoning=analysis["reasoning"],
        suggested_resolution=analysis["suggested_resolution"],
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
