from tech_news.database import db


# Requisito 10
def top_5_categories():
    news = db.news.aggregate([
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1, "_id": 1}
        }
    ])

    top_categories = [item["_id"] for item in news]
    return top_categories[:5]
