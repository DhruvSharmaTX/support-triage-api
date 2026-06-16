from app.services.groq_service import GroqService

def test_model_fallback():
    service = GroqService()
    service.llm = None
    result = service.generate_reasoning("test", "test", "General", "Low")
    assert "reasoning" in result
    assert "suggested_resolution" in result
