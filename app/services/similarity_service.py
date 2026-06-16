from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from app.services.preprocessing_service import clean_text
from app.services.groq_service import GroqService
from app.services.priority_service import adjust_priority

def find_similar_tickets(ticket_text, top_n=3):
    df = pd.read_csv("data/historical_tickets.csv")
    historical_texts = df["title"] + " " + df["description"]
    historical_texts = historical_texts.apply(clean_text)
    ticket_text = clean_text(ticket_text)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(historical_texts.tolist() + [ticket_text])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]
    df["similarity"] = similarities
    return df.sort_values(by="similarity", ascending=False).head(top_n)

def find_similar_articles(ticket_text, top_n=3):
    df = pd.read_csv("data/kb_articles.csv")
    article_texts = df["title"] + " " + df["body"]
    article_texts = article_texts.apply(clean_text)
    ticket_text = clean_text(ticket_text)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(article_texts.tolist() + [ticket_text])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]
    df["similarity"] = similarities
    return df.sort_values(by="similarity", ascending=False).head(top_n)

def predict_ticket(ticket_text: str):
    similar_tickets = find_similar_tickets(ticket_text, top_n=3)
    best_match = similar_tickets.iloc[0]
    return {
        "predicted_category": best_match["category"],
        "predicted_priority": best_match["priority"],
        "confidence": round(float(best_match["similarity"]), 2),
        "similar_ticket_id": best_match["ticket_id"],
        "similar_ticket_title": best_match["title"],
    }

def get_recommended_articles(ticket_text: str):
    articles = find_similar_articles(ticket_text, top_n=10)
    articles = articles[articles["similarity"] >= 0.10]
    recommendations = []
    for _, article in articles.head(3).iterrows():
        recommendations.append(
            {
                "article_id": article["article_id"],
                "title": article["title"],
                "category": article["category"],
                "similarity": round(float(article["similarity"]), 2),
            }
        )
    return recommendations

def analyze_ticket(title: str, description: str):
    ticket_text = f"{title} {description}"
    prediction = predict_ticket(ticket_text)
    prediction["predicted_priority"] = adjust_priority(
        ticket_text,
        prediction["predicted_priority"]
    )
    articles = get_recommended_articles(ticket_text)
    groq_service = GroqService()
    llm_response = groq_service.generate_reasoning(
        title=title,
        description=description,
        category=prediction["predicted_category"],
        priority=prediction["predicted_priority"],
    )
    return {
        "predicted_category": prediction["predicted_category"],
        "predicted_priority": prediction["predicted_priority"],
        "confidence": prediction["confidence"],
        "reasoning": llm_response["reasoning"],
        "suggested_resolution": llm_response["suggested_resolution"],
        "similar_ticket": {
            "ticket_id": prediction["similar_ticket_id"],
            "title": prediction["similar_ticket_title"],
        },
        "recommended_articles": articles,
    }
