from django.core.management.base import BaseCommand
from sports.constants import CURRENT_SEASON
from sports.data_providers.api_football_data_provider import (
    AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
    ApiFootballDataProvider,
)
from sports.league_results_importer import LeagueResultsImporter
from sports.models import Result


class Command(BaseCommand):
    help = "Import league results from the data provider API-Football"

    def handle(self, *args, **options):
        Result.objects.all().delete()
        data_provider = ApiFootballDataProvider(season=CURRENT_SEASON)
        # pass from and to here
        importer = LeagueResultsImporter(
            data_provider=data_provider,
            leagues_to_import=AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
        )
        importer.run()
