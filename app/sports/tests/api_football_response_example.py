"""
Example requests for getting premier league stadings data


```
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/standings"

querystring = {"season":"2023","league":"39"}

headers = {
	"X-RapidAPI-Key": "REPLACE-ME",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```
"""

RESPONSE_EXAMPLE = {
    "get": "standings",
    "parameters": {"league": "39", "season": "2023"},
    "errors": [],
    "results": 1,
    "paging": {"current": 1, "total": 1},
    "response": [
        {
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media-4.api-sports.io/football/leagues/39.png",
                "flag": "https://media-4.api-sports.io/flags/gb.svg",
                "season": 2023,
                "standings": [
                    [
                        {
                            "rank": 1,
                            "team": {
                                "id": 47,
                                "name": "Tottenham",
                                "logo": "https://media-4.api-sports.io/football/teams/47.png",
                            },
                            "points": 26,
                            "goalsDiff": 13,
                            "group": "Premier League",
                            "form": "WWWWD",
                            "status": "same",
                            "description": "Promotion - Champions League (Group Stage: )",
                            "all": {
                                "played": 10,
                                "win": 8,
                                "draw": 2,
                                "lose": 0,
                                "goals": {"for": 22, "against": 9},
                            },
                            "home": {
                                "played": 4,
                                "win": 4,
                                "draw": 0,
                                "lose": 0,
                                "goals": {"for": 8, "against": 2},
                            },
                            "away": {
                                "played": 6,
                                "win": 4,
                                "draw": 2,
                                "lose": 0,
                                "goals": {"for": 14, "against": 7},
                            },
                            "update": "2023-10-30T00:00:00+00:00",
                        },
                        {
                            "rank": 2,
                            "team": {
                                "id": 42,
                                "name": "Arsenal",
                                "logo": "https://media-4.api-sports.io/football/teams/42.png",
                            },
                            "points": 24,
                            "goalsDiff": 15,
                            "group": "Premier League",
                            "form": "WDWWD",
                            "status": "same",
                            "description": "Promotion - Champions League (Group Stage: )",
                            "all": {
                                "played": 10,
                                "win": 7,
                                "draw": 3,
                                "lose": 0,
                                "goals": {"for": 23, "against": 8},
                            },
                            "home": {
                                "played": 6,
                                "win": 4,
                                "draw": 2,
                                "lose": 0,
                                "goals": {"for": 15, "against": 6},
                            },
                            "away": {
                                "played": 4,
                                "win": 3,
                                "draw": 1,
                                "lose": 0,
                                "goals": {"for": 8, "against": 2},
                            },
                            "update": "2023-10-30T00:00:00+00:00",
                        },
                        {
                            "rank": 3,
                            "team": {
                                "id": 50,
                                "name": "Manchester City",
                                "logo": "https://media-4.api-sports.io/football/teams/50.png",
                            },
                            "points": 24,
                            "goalsDiff": 15,
                            "group": "Premier League",
                            "form": "WWLLW",
                            "status": "same",
                            "description": "Promotion - Champions League (Group Stage: )",
                            "all": {
                                "played": 10,
                                "win": 8,
                                "draw": 0,
                                "lose": 2,
                                "goals": {"for": 22, "against": 7},
                            },
                            "home": {
                                "played": 4,
                                "win": 4,
                                "draw": 0,
                                "lose": 0,
                                "goals": {"for": 10, "against": 2},
                            },
                            "away": {
                                "played": 6,
                                "win": 4,
                                "draw": 0,
                                "lose": 2,
                                "goals": {"for": 12, "against": 5},
                            },
                            "update": "2023-10-30T00:00:00+00:00",
                        },
                        {
                            "rank": 4,
                            "team": {
                                "id": 40,
                                "name": "Liverpool",
                                "logo": "https://media-4.api-sports.io/football/teams/40.png",
                            },
                            "points": 23,
                            "goalsDiff": 14,
                            "group": "Premier League",
                            "form": "WWDLW",
                            "status": "same",
                            "description": "Promotion - Champions League (Group Stage: )",
                            "all": {
                                "played": 10,
                                "win": 7,
                                "draw": 2,
                                "lose": 1,
                                "goals": {"for": 23, "against": 9},
                            },
                            "home": {
                                "played": 5,
                                "win": 5,
                                "draw": 0,
                                "lose": 0,
                                "goals": {"for": 14, "against": 2},
                            },
                            "away": {
                                "played": 5,
                                "win": 2,
                                "draw": 2,
                                "lose": 1,
                                "goals": {"for": 9, "against": 7},
                            },
                            "update": "2023-10-30T00:00:00+00:00",
                        },
                    ]
                ],
            }
        }
    ],
}
