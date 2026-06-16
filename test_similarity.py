from app.services.similarity_service import find_similar_tickets, predict_ticket
result1 = find_similar_tickets("Unable to receive OTP on mobile phone.")
print(result1[["ticket_id", "title", "category", "similarity"]])
result2 = predict_ticket("Unable to receive OTP on mobile phone")
print(result2)
