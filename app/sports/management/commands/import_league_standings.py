from django.core.management.base import BaseCommand
from sports.league_standings_importer import LeagueStandingsImporter
from sports.models import Team
from sports.constants import CURRENT_SEASON

from sports.data_providers.api_football_data_provider import (
    AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
    ApiFootballDataProvider,
)


class Command(BaseCommand):
    help = "Import league standings from the data provider API-Football"

    def handle(self, *args, **options):
        Team.objects.all().delete()
        data_provider = ApiFootballDataProvider(season=CURRENT_SEASON)
        importer = LeagueStandingsImporter(
            data_provider=data_provider,
            leagues_to_import=AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
        )
        importer.run()
