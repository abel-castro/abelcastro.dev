from typing import List
from sports.constants import AVAILABLE_LEAGUES, CURRENT_SEASON
from sports.models import League, Team
from sports.entities import (
    AvailableLeaguesEntity,
    LeagueInternalEntity,
    TeamInternalEntity,
)
from abc import ABC, abstractmethod


def save_team_data_to_db(team_data: List[TeamInternalEntity], league: League) -> None:
    for team in team_data:
        Team.objects.update_or_create(
            name=team.name,
            league=league,
            defaults={
                "position": team.position,
                "points": team.points,
                "logo": team.logo,
            },
        )


class DataProviderInterface(ABC):
    def __init__(self, season: int, leagues_to_import: AvailableLeaguesEntity) -> None:
        super().__init__()
        self.leagues_to_import = leagues_to_import
        self.season = season

    @abstractmethod
    def _get_data_from_data_provider(self, league_data_provider_id: int):
        NotImplemented()

    @abstractmethod
    def _transform_provider_data_to_entities(
        self, provider_data: dict
    ) -> List[TeamInternalEntity]:
        NotImplemented()

    def run(self):
        for league in self.leagues_to_import:
            league_slug = league[0]
            league_data = league[1]
            league, created = League.objects.get_or_create(
                slug=league_slug,
                defaults={
                    "name": league_data.name,
                    "logo": league_data.logo,
                },
            )
            raw_data = self._get_data_from_data_provider(
                league_data_provider_id=league_data.data_provider_id
            )
            team_entities = self._transform_provider_data_to_entities(
                provider_data=raw_data
            )
            save_team_data_to_db(team_data=team_entities, league=league)
