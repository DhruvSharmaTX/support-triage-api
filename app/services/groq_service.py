from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY, GROQ_MODEL
import json

class GroqService:
    def __init__(self):
        self.llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL, temperature=0)

    def generate_reasoning(self, title, description, category, priority):
        try:
            prompt = f"""You are a support triage assistant.
            Return ONLY valid JSON.
            {{
                "reasoning": "...",
                "suggested_resolution": "..." 
            }}
            Ticket Title:{title}
            Ticket Description:{description}
            Predicted Priority:{priority}
            Keep response under 100 words.
            """
            response = self.llm.invoke(prompt)
            return json.loads(response.content)
        except Exception:
            return {
                "reasoning": f"Ticket classified as {category} using similarity search.",
                "suggested_resolution": "Review the recommended knowledge base articles.",
            }
