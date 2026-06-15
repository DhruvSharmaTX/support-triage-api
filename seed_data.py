import pandas as pd
from app.core.database import SessionLocal
from app.models.kb_article import KBArticle
from app.models.historical_ticket import HistoricalTicket
db = SessionLocal()
# df = pd.read_csv("data/kb_articles.csv")
# for _, row in df.iterrows():
#     article = KBArticle(
#         article_id=row["article_id"],
#         title=row["title"],
#         body=row["body"],
#         category=row["category"],
#         tags=row["tags"],
#         status=row["status"],
#     )
#     db.add(article)
# db.commit()
# print("KB Articles Loaded")

df = pd.read_csv("data/historical_tickets.csv")
for _, row in df.iterrows():
    ticket = HistoricalTicket(
        ticket_id=row["ticket_id"],
        title=row["title"],
        description=row["description"],
        category=row["category"],
        priority=row["priority"],
        resolution_summary=row["resolution_summary"],
        status=row["status"],
        created_at=row["created_at"]
    )
    db.add(ticket)
db.commit()
print("Historical Tickets Loaded")