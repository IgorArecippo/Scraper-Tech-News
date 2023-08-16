import re
from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    case_insensitive_title = re.compile(title, re.IGNORECASE)
    news_found = db.news.find(
        {"title": {"$regex": case_insensitive_title}},
        {"_id": 0, "title": 1, "url": 1}
    )
    results = [(news["title"], news["url"]) for news in news_found]
    return results


# Requisito 8
def search_by_date(date):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    formatted_date = parsed_date.strftime("%d/%m/%Y")
    news_found = db.news.find(
        {"timestamp": formatted_date},
        {"_id": 0, "title": 1, "url": 1}
    )
    results = [(news["title"], news["url"]) for news in news_found]
    return results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
