from django.core.management.base import BaseCommand
from sports.models import Team
from sports.constants import CURRENT_SEASON

from sports.data_providers.api_football_data_provider import (
    AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
    ApiFootballDataProvider,
)


class Command(BaseCommand):
    help = "Import league data from the data providerAPI-Football"

    def handle(self, *args, **options):
        Team.objects.all().delete()
        data_provider = ApiFootballDataProvider(
            season=CURRENT_SEASON,
            leagues_to_import=AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA,
        )
        data_provider.run()
