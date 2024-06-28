from typing import List

from sports.constants import AVAILABLE_LEAGUES
from sports.entities import AvailableResultsEntity, ResultExternalEntity
from sports.models import League, Result


def get_current_results_data() -> AvailableResultsEntity:
    results_data = {}
    for league_slug in AVAILABLE_LEAGUES.dict():
        try:
            league = League.objects.get(slug=league_slug)
        except League.DoesNotExist:
            continue
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
        results_data[league_slug] = league_results

    return results_data


def get_latest_matchday(league_slug: str) -> int:
    matchdays: List = (
        Result.objects.filter(league__slug=league_slug)
        .distinct("matchday")
        .values_list("matchday", flat=True)
    )
    return max(matchdays) if matchdays else 0
