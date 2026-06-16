from app.services.groq_service import GroqService

groq = GroqService()
result = groq.generate_reasoning(
    title="Cannot access admin page",
    description="Permission denied error while opening settings",
    category="Access",
    priority="Medium",
)
print(result)