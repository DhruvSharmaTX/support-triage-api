from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from app.services.preprocessing_service import clean_text

# def load_historical_tickets():
#     df = pd.read_csv("data/historical_tickets.csv")
#     return df

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

def predict_ticket(ticket_text: str):
    similar_tickets = find_similar_tickets(ticket_text, top_n=3)
    best_match = similar_tickets.iloc[0]
    return {
        "predicted_category": best_match["category"],
        "predicted_priority": best_match["priority"],
        "confidence": round(float(best_match["similarity"]), 2),
        "similar_ticket_id": best_match["ticket_id"],
        "similar_ticket_title": best_match["title"]
    }
