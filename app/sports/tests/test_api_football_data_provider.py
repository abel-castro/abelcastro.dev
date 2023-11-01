from sports.data_providers.interfaces import save_team_data_to_db
import pytest
from sports.models import League, Team
from sports.tests.api_football_response_example import RESPONSE_EXAMPLE
from sports.data_providers.api_football_data_provider import (
    transform_provider_data_to_entities,
)
from sports.entities import LeagueInternalEntity, TeamInternalEntity


TEST_TEAM_ENTITY_LIST = [
    TeamInternalEntity(
        name="Tottenham",
        data_provider_id=47,
        points=26,
        position=1,
        logo="https://media-4.api-sports.io/football/teams/47.png",
    ),
    TeamInternalEntity(
        name="Arsenal",
        data_provider_id=42,
        points=24,
        position=2,
        logo="https://media-4.api-sports.io/football/teams/42.png",
    ),
    TeamInternalEntity(
        name="Manchester City",
        data_provider_id=50,
        points=24,
        position=3,
        logo="https://media-4.api-sports.io/football/teams/50.png",
    ),
    TeamInternalEntity(
        name="Liverpool",
        data_provider_id=40,
        points=23,
        position=4,
        logo="https://media-4.api-sports.io/football/teams/40.png",
    ),
]


@pytest.mark.django_db()
def test_save_team_data_to_db():
    premier_league = League.objects.create(
        name="Premier League",
        slug="english_premier_league",
        logo="https://media-4.api-sports.io/football/leagues/39.png",
    )
    assert League.objects.count() == 1
    assert Team.objects.count() == 0
    save_team_data_to_db(team_data=TEST_TEAM_ENTITY_LIST, league=premier_league)
    assert League.objects.count() == 1
    assert Team.objects.count() == 4


def test_transform_provider_data_to_entities():
    assert (
        transform_provider_data_to_entities(provider_data=RESPONSE_EXAMPLE)
        == TEST_TEAM_ENTITY_LIST
    )
