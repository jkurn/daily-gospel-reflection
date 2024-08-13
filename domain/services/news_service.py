from data.repositories.news_repository import NewsRepository
from domain.entities.news import NewsItem
from typing import List

class NewsService:
    @staticmethod
    def get_top_news(limit: int = 5) -> List[NewsItem]:
        return NewsRepository.get_top_news(limit)
