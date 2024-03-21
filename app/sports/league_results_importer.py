from typing import List

from django.utils import timezone
from sports.data_providers.interfaces import DataProviderInterface
from sports.entities import (
    AvailableLeaguesEntity,
    LeagueInternalEntity,
    ResultInternalEntity,
)
from sports.models import League, Result


def save_team_data_to_db(
    results_data: List[ResultInternalEntity], league: League
) -> None:
    for result_entity in results_data:
        Result.objects.update_or_create(
            homeTeam=result_entity.homeTeam,
            awayTeam=result_entity.awayTeam,
            league=league,
            defaults={
                "homeScore": result_entity.homeScore,
                "awayScore": result_entity.awayScore,
                "matchday": result_entity.matchday,
            },
        )
    if result_entity:
        league.updated_at = timezone.now()
        league.save()


class LeagueResultsImporter:
    def __init__(
        self,
        data_provider: DataProviderInterface,
        leagues_to_import: AvailableLeaguesEntity,
        from_date: str,
        to_date: str,
    ) -> None:
        super().__init__()
        self.data_provider = data_provider
        self.leagues_to_import = leagues_to_import
        self.from_date = from_date
        self.to_date = to_date

    @staticmethod
    def get_or_create_league(
        league_slug: str, league_data: LeagueInternalEntity
    ) -> League:
        league, _ = League.objects.get_or_create(
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
            raw_data = self.data_provider.get_raw_results_data(
                league_data_provider_id=league_entity.data_provider_id,
                from_date=self.from_date,
                to_date=self.to_date,
            )
            result_entities = self.data_provider.transform_raw_results_data_to_entities(
                provider_data=raw_data
            )
            save_team_data_to_db(results_data=result_entities, league=league_instance)
