from app.models.analysis_result import AnalysisResult
def get_analysis_history(db):
    return (
        db.query(AnalysisResult).order_by(AnalysisResult.id.desc()).all()
    )
