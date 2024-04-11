import pytest
from sports.entities import LeagueExternalEntity, ResultExternalEntity
from sports.get_current_results_data_from_db import get_current_results_data, get_latest_matchday
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

    Result.objects.create(
        homeTeam="Fulham",
        awayTeam="Tottenham",
        homeScore=3,
        awayScore=0,
        league=premier_league,
        matchday=2,
    )

    Result.objects.create(
        homeTeam="Aston Villa",
        awayTeam="Wolves",
        homeScore=2,
        awayScore=0,
        league=premier_league,
        matchday=2,
    )

@pytest.mark.django_db()
def test_get_current_results_data():
    create_test_data()

    ResultExternalEntity(
        homeTeam="Tottenham Hotspur",
        awayTeam="Arsenal",
        homeScore=1,
        awayScore=2,
        matchday=1,
    )

    ResultExternalEntity(
        homeTeam="Man. City", awayTeam="Chelsea", homeScore=3, awayScore=5, matchday=1
    )

    result_3 = ResultExternalEntity(
        homeTeam="Fulham", awayTeam="Tottenham", homeScore=3, awayScore=0, matchday=2
    )

    result_4 = ResultExternalEntity(
        homeTeam="Aston Villa", awayTeam="Wolves", homeScore=2, awayScore=0, matchday=2
    )

    expected_data = {
        "english_premier_league": [
            result_3.dict(),
            result_4.dict(),
        ]
    }

    assert get_current_results_data() == expected_data


@pytest.mark.django_db()
def test_get_latest_matchday():
    create_test_data()

    assert get_latest_matchday(league_slug="english_premier_league") == 2


@pytest.mark.django_db()
def test_get_latest_matchday__no_results():
    assert get_latest_matchday(league_slug="english_premier_league") == 0