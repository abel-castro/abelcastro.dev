from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from sports.utils import get_date_30_days_ago
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
        from_date_string = get_date_30_days_ago().isoformat()
        to_date_string = (timezone.now() - timedelta(days=1)).date().isoformat()

        importer = LeagueResultsImporter(
            data_provider=data_provider,
            leagues_to_import=AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
            from_date=from_date_string,
            to_date=to_date_string,
        )
        importer.run()
