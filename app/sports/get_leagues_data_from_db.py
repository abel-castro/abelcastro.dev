from typing import List

from sports.constants import AVAILABLE_LEAGUES
from sports.entities import (LeagueExternalEntity, ResultExternalEntity,
                             TeamExternalEntity)
from sports.get_current_results_data_from_db import get_latest_matchday
from sports.models import League


def get_current_standings_data() -> List[LeagueExternalEntity]:
    leagues_data = []
    for league_slug in AVAILABLE_LEAGUES.dict():
        league_teams = []
        league_name = ""
        league_logo = ""

        league, created = League.objects.get_or_create(slug=league_slug)
        teams = league.teams
        league_name = league.name
        league_logo = league.logo

        for team in teams.order_by("position"):
            league_teams.append(
                TeamExternalEntity(
                    name=team.name,
                    position=team.position,
                    points=team.points,
                    logo=team.logo,
                ).dict()
            )

        # results
        latest_matchday = get_latest_matchday(league_slug=league_slug)
        results = league.results.filter(matchday=latest_matchday)
        league_results = []
        for result in results:
            result_data = ResultExternalEntity(
                homeTeam=result.homeTeam,
                awayTeam=result.awayTeam,
                homeScore=result.homeScore,
                awayScore=result.awayScore,
                matchday=result.matchday,
            )
            league_results.append(result_data.dict())

        if league_name and league_teams:
            leagues_data.append(
                LeagueExternalEntity(
                    name=league_name,
                    slug=league.slug,
                    teams=league_teams,
                    logo=league_logo,
                    results=league_results,
                ).dict()
            )

    return leagues_data
