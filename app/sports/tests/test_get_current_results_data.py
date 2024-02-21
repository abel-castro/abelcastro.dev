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
        team_1="Tottenham Hotspur",
        team_2="Arsenal",
        team_1_goals=1,
        team_2_goals=2,
        league=premier_league,
        matchday=1,
    )

    Result.objects.create(
        team_1="Man. City",
        team_2="Chelsea",
        team_1_goals=3,
        team_2_goals=5,
        league=premier_league,
        matchday=1,
    )


@pytest.mark.django_db()
def test_get_current_results_data():
    create_test_data()

    result_1 = ResultExternalEntity(
        team_1="Tottenham Hotspur",
        team_2="Arsenal",
        team_1_goals=1,
        team_2_goals=2,
        matchday=1,
    )

    result_2 = ResultExternalEntity(
        team_1="Man. City", team_2="Chelsea", team_1_goals=3, team_2_goals=5, matchday=1
    )

    expected_data = {
        "english_premier_league": [
            result_1.dict(),
            result_2.dict(),
        ]
    }

    assert get_current_results_data() == expected_data
