from django.utils import timezone
from typing import List
from sports.data_providers.interfaces import DataProviderInterface
from sports.entities import (
    AvailableLeaguesEntity,
    LeagueInternalEntity,
    TeamInternalEntity,
)
from sports.models import League, Team


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
    if team_data:
        league.updated_at = timezone.now()


class LeagueStandingsImporter:
    def __init__(
        self,
        data_provider: DataProviderInterface,
        leagues_to_import: AvailableLeaguesEntity,
    ) -> None:
        super().__init__()
        self.data_provider = data_provider
        self.leagues_to_import = leagues_to_import

    @staticmethod
    def get_or_create_league(
        league_slug: str, league_data: LeagueInternalEntity
    ) -> League:
        league, created = League.objects.get_or_create(
            slug=league_slug,
            defaults={
                "name": league_data.name,
                "logo": league_data.logo,
            },
        )
        return league

    def run(self) -> None:
        for league_to_import in self.leagues_to_import:
            league_slug = league_to_import[0]
            league_entity = league_to_import[1]
            league_instance = self.get_or_create_league(
                league_slug=league_slug, league_data=league_entity
            )
            raw_data = self.data_provider.get_raw_data(
                league_data_provider_id=league_entity.data_provider_id
            )
            team_entities = self.data_provider.transform_raw_data_to_entities(
                provider_data=raw_data
            )
            save_team_data_to_db(team_data=team_entities, league=league_instance)
