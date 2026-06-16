from app.services.similarity_service import (
    find_similar_tickets,
    find_similar_articles,
    predict_ticket,
    analyze_ticket,
)

tickets = find_similar_tickets("Unable to receive OTP on mobile phone.")
print(tickets[["ticket_id", "title", "category", "similarity"]], "\n")
predictions = predict_ticket("Unable to receive OTP on mobile phone")
print(predictions, "\n")
articles = find_similar_articles("Permission denied while opening admin page")
print(articles[["article_id", "title", "category", "similarity"]], "\n")
analysis = analyze_ticket(
    title="Cannot access admin page",
    description="Premission denied error while opening settings",
)
print(analysis)
