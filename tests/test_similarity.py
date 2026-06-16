from app.services.similarity_service import get_recommended_articles

def test_similarity_articles():
    articles = get_recommended_articles("Permission denied while opening admin page")
    assert len(articles) > 0
    assert articles[0]["article_id"] == "KB-003"
