import pandas as pd
from app.core.database import SessionLocal
from app.models.kb_article import KBArticle
from app.models.historical_ticket import HistoricalTicket
def seed_kb_articles(db):
    df = pd.read_csv("data/kb_articles.csv")
    count = 0
    for _, row in df.iterrows():
        exists = (
            db.query(KBArticle)
            .filter(KBArticle.article_id == row["article_id"])
            .first()
        )
        if exists:
            continue
        article = KBArticle(
            article_id=row["article_id"],
            title=row["title"],
            body=row["body"],
            category=row["category"],
            tags=row["tags"],
            status=row["status"],
        )
        db.add(article)
        count += 1
    db.commit()
    print(f"Loaded {count} KB Articles")

def seed_historical_tickets(db):
    df = pd.read_csv("data/historical_tickets.csv")
    count = 0
    for _, row in df.iterrows():
        exists = (
            db.query(HistoricalTicket)
            .filter(HistoricalTicket.ticket_id == row["ticket_id"])
            .first()
        )
        if exists:
            continue
        ticket = HistoricalTicket(
            ticket_id=row["ticket_id"],
            title=row["title"],
            description=row["description"],
            category=row["category"],
            priority=row["priority"],
            resolution_summary=row["resolution_summary"],
            status=row["status"],
            created_at=row["created_at"],
        )
        db.add(ticket)
        count += 1
    db.commit()
    print(f"Loaded {count} Historical Tickets")

def seed_database():
    db = SessionLocal()
    try:
        seed_kb_articles(db)
        seed_historical_tickets(db)
        print("Database Seeding Complete")
    except Exception as e:
        db.rollback()
        print(f"Seeding Failed: {e}")
    finally:
        db.close()
        
if __name__ == "__main__":
    seed_database()