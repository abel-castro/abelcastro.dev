from sports.entities import TeamInternalEntity, ResultInternalEntity

TEST_TEAM_STANDINGS_ENTITY_LIST = [
    TeamInternalEntity(
        name="Tottenham",
        data_provider_id=47,
        points=26,
        position=1,
        logo="https://media-4.api-sports.io/football/teams/47.png",
    ),
    TeamInternalEntity(
        name="Arsenal",
        data_provider_id=42,
        points=24,
        position=2,
        logo="https://media-4.api-sports.io/football/teams/42.png",
    ),
    TeamInternalEntity(
        name="Manchester City",
        data_provider_id=50,
        points=24,
        position=3,
        logo="https://media-4.api-sports.io/football/teams/50.png",
    ),
    TeamInternalEntity(
        name="Liverpool",
        data_provider_id=40,
        points=23,
        position=4,
        logo="https://media-4.api-sports.io/football/teams/40.png",
    ),
]


TEST_RESULT_ENTITY_LIST = [
    ResultInternalEntity(
        homeTeam="Bournemouth",
        awayTeam="Luton",
        homeScore=4,
        awayScore=3,
        matchday=17,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Chelsea",
        awayTeam="Newcastle",
        homeScore=3,
        awayScore=2,
        matchday=28,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Burnley",
        awayTeam="Brentford",
        homeScore=2,
        awayScore=1,
        matchday=29,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Fulham",
        awayTeam="Tottenham",
        homeScore=3,
        awayScore=0,
        matchday=29,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Luton",
        awayTeam="Nottingham Forest",
        homeScore=1,
        awayScore=1,
        matchday=29,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="West Ham",
        awayTeam="Aston Villa",
        homeScore=1,
        awayScore=1,
        matchday=29,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Bournemouth",
        awayTeam="Everton",
        homeScore=2,
        awayScore=1,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Aston Villa",
        awayTeam="Wolves",
        homeScore=2,
        awayScore=0,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Brentford",
        awayTeam="Manchester United",
        homeScore=1,
        awayScore=1,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Chelsea",
        awayTeam="Burnley",
        homeScore=2,
        awayScore=2,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Liverpool",
        awayTeam="Brighton",
        homeScore=2,
        awayScore=1,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Manchester City",
        awayTeam="Arsenal",
        homeScore=0,
        awayScore=0,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Newcastle",
        awayTeam="West Ham",
        homeScore=4,
        awayScore=3,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Nottingham Forest",
        awayTeam="Crystal Palace",
        homeScore=1,
        awayScore=1,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Sheffield Utd",
        awayTeam="Fulham",
        homeScore=3,
        awayScore=3,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Tottenham",
        awayTeam="Luton",
        homeScore=2,
        awayScore=1,
        matchday=30,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Bournemouth",
        awayTeam="Crystal Palace",
        homeScore=1,
        awayScore=0,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Arsenal",
        awayTeam="Luton",
        homeScore=2,
        awayScore=0,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Brentford",
        awayTeam="Brighton",
        homeScore=0,
        awayScore=0,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Burnley",
        awayTeam="Wolves",
        homeScore=1,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Nottingham Forest",
        awayTeam="Fulham",
        homeScore=3,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="West Ham",
        awayTeam="Tottenham",
        homeScore=1,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Chelsea",
        awayTeam="Manchester United",
        homeScore=4,
        awayScore=3,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Newcastle",
        awayTeam="Everton",
        homeScore=1,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Liverpool",
        awayTeam="Sheffield Utd",
        homeScore=3,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Manchester City",
        awayTeam="Aston Villa",
        homeScore=4,
        awayScore=1,
        matchday=31,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Aston Villa",
        awayTeam="Brentford",
        homeScore=3,
        awayScore=3,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Brighton",
        awayTeam="Arsenal",
        homeScore=0,
        awayScore=3,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Crystal Palace",
        awayTeam="Manchester City",
        homeScore=2,
        awayScore=4,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Everton",
        awayTeam="Burnley",
        homeScore=1,
        awayScore=0,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Fulham",
        awayTeam="Newcastle",
        homeScore=0,
        awayScore=1,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Luton",
        awayTeam="Bournemouth",
        homeScore=2,
        awayScore=1,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Manchester United",
        awayTeam="Liverpool",
        homeScore=2,
        awayScore=2,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Sheffield Utd",
        awayTeam="Chelsea",
        homeScore=2,
        awayScore=2,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Tottenham",
        awayTeam="Nottingham Forest",
        homeScore=3,
        awayScore=1,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
    ResultInternalEntity(
        homeTeam="Wolves",
        awayTeam="West Ham",
        homeScore=1,
        awayScore=2,
        matchday=32,
        id=None,
        data_provider_league_id=39,
    ),
]
