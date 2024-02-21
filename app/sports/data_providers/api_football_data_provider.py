import copy
from typing import List

import requests
from django.conf import settings
from sports.constants import AVAILABLE_LEAGUES
from sports.data_providers.interfaces import DataProviderInterface
from sports.entities import AvailableLeaguesEntity, TeamInternalEntity


def add_api_football_related_data() -> AvailableLeaguesEntity:
    available_leagues_with_api_football_data = copy.deepcopy(AVAILABLE_LEAGUES)

    available_leagues_with_api_football_data.english_premier_league.data_provider_id = (
        39
    )

    available_leagues_with_api_football_data.english_premier_league.logo = (
        "https://media-4.api-sports.io/football/leagues/39.png"
    )

    available_leagues_with_api_football_data.spanish_la_liga.data_provider_id = 140
    available_leagues_with_api_football_data.spanish_la_liga.logo = (
        "https://media-4.api-sports.io/football/leagues/140.png"
    )

    available_leagues_with_api_football_data.italian_seria_a.data_provider_id = 135
    available_leagues_with_api_football_data.italian_seria_a.logo = (
        "https://media-4.api-sports.io/football/leagues/135.png"
    )

    available_leagues_with_api_football_data.german_bundesliga.data_provider_id = 78
    available_leagues_with_api_football_data.german_bundesliga.logo = (
        "https://media-4.api-sports.io/football/leagues/78.png"
    )

    available_leagues_with_api_football_data.austrian_bundesliga.data_provider_id = 218
    available_leagues_with_api_football_data.austrian_bundesliga.logo = (
        "https://media-4.api-sports.io/football/leagues/218.png"
    )

    available_leagues_with_api_football_data.french_ligue_1.data_provider_id = 61
    available_leagues_with_api_football_data.french_ligue_1.logo = (
        "https://media-4.api-sports.io/football/leagues/61.png"
    )

    available_leagues_with_api_football_data.portuguese_primeira_liga.data_provider_id = (
        94
    )
    available_leagues_with_api_football_data.portuguese_primeira_liga.logo = (
        "https://media-4.api-sports.io/football/leagues/94.png"
    )
    return available_leagues_with_api_football_data


AVAILABLE_LEAGUES_WITH_API_FOOTBALL_DATA = add_api_football_related_data()


def transform_provider_data_to_entities(
    provider_data: dict,
) -> List[TeamInternalEntity]:
    result = []
    try:
        league_data = provider_data.get("response")[0]
        for team_data in league_data.get("league").get("standings")[0]:
            team_name = team_data.get("team").get("name")
            team_logo = team_data.get("team").get("logo")
            team_position = team_data.get("rank")
            team_points = team_data.get("points")
            team_id = team_data.get("team").get("id")
            result.append(
                TeamInternalEntity(
                    name=team_name,
                    logo=team_logo,
                    position=team_position,
                    points=team_points,
                    data_provider_id=team_id,
                )
            )
    except KeyError:
        pass
    return result


class ApiFootballDataProvider(DataProviderInterface):
    def get_raw_data(self, league_data_provider_id: int) -> dict:
        data = {}
        url = "https://api-football-v1.p.rapidapi.com/v3/standings"

        querystring = {"season": self.season, "league": league_data_provider_id}

        headers = {
            "X-RapidAPI-Key": settings.API_FOOTBAL_KEY,
            "X-RapidAPI-Host": settings.API_FOOTBAL_HOST,
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            return response.json()
        except:
            pass

        return data

    def transform_raw_data_to_entities(
        self, provider_data: dict
    ) -> List[TeamInternalEntity]:
        return transform_provider_data_to_entities(provider_data=provider_data)
