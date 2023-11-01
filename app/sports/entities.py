from pydantic import BaseModel
from typing import List, Optional


class TeamExternalEntity(BaseModel):
    position: int
    name: str
    points: int
    logo: Optional[str] = None


class TeamInternalEntity(TeamExternalEntity):
    id: Optional[int] = None
    data_provider_id: Optional[int] = None


class LeagueExternalEntity(BaseModel):
    name: str
    slug: str
    teams: List[TeamExternalEntity] = []
    logo: Optional[str] = None


class LeagueInternalEntity(LeagueExternalEntity):
    id: Optional[int] = None
    data_provider_id: Optional[int] = None
    teams: List[TeamInternalEntity] = []


class AvailableLeaguesEntity(BaseModel):
    english_premier_league: LeagueInternalEntity
    spanish_la_liga: LeagueInternalEntity
    italian_seria_a: LeagueInternalEntity
    german_bundesliga: LeagueInternalEntity
    austrian_bundesliga: LeagueInternalEntity
    french_ligue_1: LeagueInternalEntity
