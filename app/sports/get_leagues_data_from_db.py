from typing import List
from sports.constants import AVAILABLE_LEAGUES
from sports.models import League
from sports.entities import (
    TeamExternalEntity,
    LeagueExternalEntity,
)


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

        if league_name and league_teams:
            leagues_data.append(
                LeagueExternalEntity(
                    name=league_name,
                    slug=league.slug,
                    teams=league_teams,
                    logo=league_logo,
                ).dict()
            )

    return leagues_data
