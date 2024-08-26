RESULTS_API_EXAMPLE = {
    "english_premier_league": [
        {
            "matchday": 1,
            "homeTeam": "Tottenham Hotspur",
            "homeScore": 1,
            "awayTeam": "Arsenal",
            "awayScore": 2,
        }
    ],
    "spanish_la_liga": [],
    "italian_seria_a": [],
    "german_bundesliga": [],
    "french_ligue_1": [],
    "portuguese_primeira_liga": [],
}


STANDINGS_API_EXAMPLE = [
    {
        "name": "Premier League",
        "slug": "english_premier_league",
        "logo": "https://media-4.api-sports.io/football/leagues/39.png",
        "teams": [
            {
                "position": 1,
                "name": "Manchester City",
                "points": 27,
                "logo": "https://media-4.api-sports.io/football/teams/50.png",
            }
        ],
        "results": [
            {
                "matchday": 1,
                "team_1": "Tottenham Hotspur",
                "team_1_goals": 1,
                "team_2": "Arsenal",
                "team_2_goals": 2,
            },
        ],
    },
]
