from sports.entities import AvailableLeaguesEntity, LeagueInternalEntity

CURRENT_SEASON = 2023


AVAILABLE_LEAGUES = AvailableLeaguesEntity(
    english_premier_league=LeagueInternalEntity(
        name="Premier League",
        slug="english_premier_league",
    ),
    spanish_la_liga=LeagueInternalEntity(name="La Liga", slug="spanish_la_liga"),
    italian_seria_a=LeagueInternalEntity(name="Serie A", slug="italian_seria_a"),
    german_bundesliga=LeagueInternalEntity(
        name="German Bundesliga", slug="german_bundesliga"
    ),
    austrian_bundesliga=LeagueInternalEntity(
        name="Austrian Bundesliga", slug="austrian_bundesliga"
    ),
    french_ligue_1=LeagueInternalEntity(
        name="Ligue 1",
        slug="french_ligue_1",
    ),
    portuguese_primeira_liga=LeagueInternalEntity(
        name="Primeira Liga",
        slug="portuguese_primeira_liga",
    ),
)
