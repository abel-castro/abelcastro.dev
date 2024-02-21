from abc import ABC, abstractmethod
from typing import List

from sports.entities import AvailableLeaguesEntity, TeamInternalEntity


class DataProviderInterface(ABC):
    def __init__(self, season: int) -> None:
        super().__init__()
        self.season = season

    @abstractmethod
    def get_raw_data(self, league_data_provider_id: int):
        NotImplemented()

    @abstractmethod
    def transform_raw_data_to_entities(
        self, provider_data: dict
    ) -> List[TeamInternalEntity]:
        NotImplemented()
