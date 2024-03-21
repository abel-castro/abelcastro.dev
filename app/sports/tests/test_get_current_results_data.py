import pytest
from sports.entities import LeagueExternalEntity, ResultExternalEntity
from sports.get_current_results_data_from_db import get_current_results_data
from sports.models import League, Result, Team


def create_test_data():
    premier_league = League.objects.create(
        name="Premier League",
        slug="english_premier_league",
        logo="https://media-4.api-sports.io/football/leagues/39.png",
    )
    Result.objects.create(
        homeTeam="Tottenham Hotspur",
        awayTeam="Arsenal",
        homeScore=1,
        awayScore=2,
        league=premier_league,
        matchday=1,
    )

    Result.objects.create(
        homeTeam="Man. City",
        awayTeam="Chelsea",
        homeScore=3,
        awayScore=5,
        league=premier_league,
        matchday=1,
    )


@pytest.mark.django_db()
def test_get_current_results_data():
    create_test_data()

    result_1 = ResultExternalEntity(
        homeTeam="Tottenham Hotspur",
        awayTeam="Arsenal",
        homeScore=1,
        awayScore=2,
        matchday=1,
    )

    result_2 = ResultExternalEntity(
        homeTeam="Man. City", awayTeam="Chelsea", homeScore=3, awayScore=5, matchday=1
    )

    expected_data = {
        "english_premier_league": [
            result_1.dict(),
            result_2.dict(),
        ]
    }

    assert get_current_results_data() == expected_data
