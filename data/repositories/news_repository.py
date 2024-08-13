from data.datasources.news_datasource import fetch_top_news
from domain.entities.news import NewsItem
from typing import List

class NewsRepository:
    @staticmethod
    def get_top_news(limit: int = 5) -> List[NewsItem]:
        # Fetch news and convert to list of NewsItem entities
        pass
