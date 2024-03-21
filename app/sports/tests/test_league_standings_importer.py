import pytest
from sports.league_standings_importer import save_team_data_to_db
from sports.models import League, Team
from sports.tests.test_api_football_data_provider import TEST_TEAM_STANDINGS_ENTITY_LIST


@pytest.mark.django_db()
def test_save_team_data_to_db():
    premier_league = League.objects.create(
        name="Premier League",
        slug="english_premier_league",
        logo="https://media-4.api-sports.io/football/leagues/39.png",
    )
    assert League.objects.count() == 1
    assert Team.objects.count() == 0
    save_team_data_to_db(
        team_data=TEST_TEAM_STANDINGS_ENTITY_LIST, league=premier_league
    )
    assert League.objects.count() == 1
    assert Team.objects.count() == 4
