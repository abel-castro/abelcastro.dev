import pytest
from sports.entities import LeagueExternalEntity
from sports.get_leagues_data_from_db import get_current_standings_data
from sports.models import League, Team

TEST_PREMIER_LEAGUE_TEAMS = [
    {"position": 1, "name": "Tottenham Hotspur", "points": 20},
    {"position": 2, "name": "Arsenal", "points": 18},
    {"position": 3, "name": "Man. City", "points": 15},
    {"position": 4, "name": "Man. U", "points": 13},
    {"position": 5, "name": "Newcastle", "points": 12},
    {"position": 6, "name": "Brighton", "points": 10},
    {"position": 7, "name": "Chelsea", "points": 9},
]

TEST_LA_LIGA_TEAMS = [
    {"position": 1, "name": "FC Barcelona", "points": 20},
    {"position": 2, "name": "Real Madrid", "points": 19},
    {"position": 3, "name": "Girona", "points": 18},
    {"position": 4, "name": "Atlético de Madrid", "points": 16},
    {"position": 5, "name": "Athletic Bilbao", "points": 14},
    {"position": 6, "name": "Villareal", "points": 13},
    {"position": 7, "name": "Real Sociedad", "points": 1},
]


def create_test_data():
    premier_league = League.objects.create(
        name="Premier League",
        slug="english_premier_league",
        logo="https://media-4.api-sports.io/football/leagues/39.png",
    )
    for team in TEST_PREMIER_LEAGUE_TEAMS:
        Team.objects.create(
            name=team["name"],
            position=team["position"],
            points=team["points"],
            league=premier_league,
        )

    la_liga = League.objects.create(
        name="La Liga",
        slug="spanish_la_liga",
        logo="https://media-4.api-sports.io/football/leagues/140.png",
    )
    for team in TEST_LA_LIGA_TEAMS:
        Team.objects.create(
            name=team["name"],
            position=team["position"],
            points=team["points"],
            league=la_liga,
        )


@pytest.mark.django_db()
def test_get_current_standings_data():
    create_test_data()

    premier_league = LeagueExternalEntity(
        name="Premier League",
        slug="english_premier_league",
        teams=TEST_PREMIER_LEAGUE_TEAMS,
        logo="https://media-4.api-sports.io/football/leagues/39.png",
    )
    la_liga = LeagueExternalEntity(
        name="La Liga",
        slug="spanish_la_liga",
        teams=TEST_LA_LIGA_TEAMS,
        logo="https://media-4.api-sports.io/football/leagues/140.png",
    )

    expected_data = [
        premier_league.dict(),
        la_liga.dict(),
    ]

    assert get_current_standings_data() == expected_data
