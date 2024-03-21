from typing import List, Optional

from pydantic import BaseModel


class TeamExternalEntity(BaseModel):
    position: int
    name: str
    points: int
    logo: Optional[str] = None


class TeamInternalEntity(TeamExternalEntity):
    id: Optional[int] = None
    data_provider_id: Optional[int] = None


class ResultExternalEntity(BaseModel):
    homeTeam: str
    awayTeam: str
    homeScore: int
    awayScore: int
    matchday: int

class LeagueExternalEntity(BaseModel):
    name: str
    slug: str
    teams: List[TeamExternalEntity] = []
    logo: Optional[str] = None
    results: Optional[List[ResultExternalEntity]] = []


class LeagueInternalEntity(LeagueExternalEntity):
    id: Optional[int] = None
    data_provider_id: Optional[int] = None
    teams: List[TeamInternalEntity] = []


class ResultInternalEntity(ResultExternalEntity):
    id: Optional[int] = None
    data_provider_league_id: Optional[int] = None


class AvailableLeaguesEntity(BaseModel):
    english_premier_league: LeagueInternalEntity
    spanish_la_liga: LeagueInternalEntity
    italian_seria_a: LeagueInternalEntity
    german_bundesliga: LeagueInternalEntity
    austrian_bundesliga: LeagueInternalEntity
    french_ligue_1: LeagueInternalEntity
    portuguese_primeira_liga: LeagueInternalEntity


class AvailableResultsEntity(BaseModel):
    english_premier_league: Optional[List[ResultExternalEntity]] = []
    spanish_la_liga: Optional[List[ResultExternalEntity]] = []
    italian_seria_a: Optional[List[ResultExternalEntity]] = []
    german_bundesliga: Optional[List[ResultExternalEntity]] = []
    austrian_bundesliga: Optional[List[ResultExternalEntity]] = []
    french_ligue_1: Optional[List[ResultExternalEntity]] = []
    portuguese_primeira_liga: Optional[List[ResultExternalEntity]] = []
