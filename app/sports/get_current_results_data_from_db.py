from typing import List

from sports.constants import AVAILABLE_LEAGUES
from sports.entities import AvailableResultsEntity, ResultExternalEntity
from sports.models import League


def get_current_results_data() -> AvailableResultsEntity:
    results_data = {}
    for league_slug in AVAILABLE_LEAGUES.dict():
        try:
            league = League.objects.get(slug=league_slug)
        except League.DoesNotExist:
            continue
        results = league.results.all()
        league_results = []
        for result in results:
            result_data = ResultExternalEntity(
                team_1=result.team_1,
                team_2=result.team_2,
                team_1_goals=result.team_1_goals,
                team_2_goals=result.team_2_goals,
                matchday=result.matchday,
            )
            league_results.append(result_data.dict())
        results_data[league_slug] = league_results

    return results_data
