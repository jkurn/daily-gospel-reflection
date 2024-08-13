from data.repositories.gospel_repository import GospelRepository
from domain.entities.gospel import Gospel

class GospelService:
    @staticmethod
    def get_daily_gospel() -> Gospel:
        return GospelRepository.get_daily_gospel()
