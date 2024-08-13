from data.datasources.gospel_datasource import fetch_daily_gospel
from domain.entities.gospel import Gospel

class GospelRepository:
    @staticmethod
    def get_daily_gospel() -> Gospel:
        # Fetch gospel and convert to Gospel entity
        pass
