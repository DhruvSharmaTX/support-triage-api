from app.models.analysis_result import AnalysisResult
from sqlalchemy import func

def get_analytics_summary(db):
    total_requests = db.query(AnalysisResult).count()
    categories = (
        db.query(AnalysisResult.predicted_category, func.count().label("count"))
        .group_by(AnalysisResult.predicted_category)
        .all()
    )
    priorities = (
        db.query(AnalysisResult.predicted_priority, func.count().label("count"))
        .group_by(AnalysisResult.predicted_priority)
        .all()
    )
    latest = db.query(AnalysisResult).order_by(AnalysisResult.id.desc()).limit(5).all()
    return {
        "total_requests": total_requests,
        "category_summary": {row.predicted_category: row.count for row in categories},
        "priority_summary": {row.predicted_priority: row.count for row in priorities},
        "latest_requests": [{"id": item.id, "title": item.title} for item in latest],
    }
