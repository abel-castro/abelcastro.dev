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

STANDINGS_RESPONSE_EXAMPLE = {
    "get": "fixtures",
    "parameters": {
        "league": "140",
        "from": "2024-03-14",
        "to": "2024-03-19",
        "season": "2023",
    },
    "errors": [],
    "results": 10,
    "paging": {"current": 1, "total": 1},
    "response": [
        {
            "fixture": {
                "id": 1038232,
                "referee": "Jose Maria Sanchez Martinez, Spain",
                "timezone": "UTC",
                "date": "2024-03-17T20:00:00+00:00",
                "timestamp": 1710705600,
                "periods": {"first": 1710705600, "second": 1710709200},
                "venue": {
                    "id": 19217,
                    "name": "Estádio Cívitas Metropolitano",
                    "city": "Madrid",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 530,
                    "name": "Atletico Madrid",
                    "logo": "https://media.api-sports.io/football/teams/530.png",
                    "winner": False,
                },
                "away": {
                    "id": 529,
                    "name": "Barcelona",
                    "logo": "https://media.api-sports.io/football/teams/529.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 3},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 0, "away": 3},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038233,
                "referee": "José Luis Munuera Montero, Spain",
                "timezone": "UTC",
                "date": "2024-03-16T17:30:00+00:00",
                "timestamp": 1710610200,
                "periods": {"first": 1710610200, "second": 1710613800},
                "venue": {"id": 20422, "name": "Estadio Coliseum", "city": "Getafe"},
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 546,
                    "name": "Getafe",
                    "logo": "https://media.api-sports.io/football/teams/546.png",
                    "winner": True,
                },
                "away": {
                    "id": 547,
                    "name": "Girona",
                    "logo": "https://media.api-sports.io/football/teams/547.png",
                    "winner": False,
                },
            },
            "goals": {"home": 1, "away": 0},
            "score": {
                "halftime": {"home": 1, "away": 0},
                "fulltime": {"home": 1, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038234,
                "referee": "Juan Martinez Munuera, Spain",
                "timezone": "UTC",
                "date": "2024-03-16T15:15:00+00:00",
                "timestamp": 1710602100,
                "periods": {"first": 1710602100, "second": 1710605700},
                "venue": {"id": 1486, "name": "Estadio El Sadar", "city": "Iruñea"},
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 727,
                    "name": "Osasuna",
                    "logo": "https://media.api-sports.io/football/teams/727.png",
                    "winner": False,
                },
                "away": {
                    "id": 541,
                    "name": "Real Madrid",
                    "logo": "https://media.api-sports.io/football/teams/541.png",
                    "winner": True,
                },
            },
            "goals": {"home": 2, "away": 4},
            "score": {
                "halftime": {"home": 1, "away": 2},
                "fulltime": {"home": 2, "away": 4},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038235,
                "referee": "Victor Garcia Verdura, Spain",
                "timezone": "UTC",
                "date": "2024-03-17T15:15:00+00:00",
                "timestamp": 1710688500,
                "periods": {"first": 1710688500, "second": 1710692100},
                "venue": {
                    "id": 1481,
                    "name": "Estadio de Gran Canaria",
                    "city": "Las Palmas de Gran Canaria",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 534,
                    "name": "Las Palmas",
                    "logo": "https://media.api-sports.io/football/teams/534.png",
                    "winner": False,
                },
                "away": {
                    "id": 723,
                    "name": "Almeria",
                    "logo": "https://media.api-sports.io/football/teams/723.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 0, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038236,
                "referee": "Juan Luis Pulido Santana, Spain",
                "timezone": "UTC",
                "date": "2024-03-17T17:30:00+00:00",
                "timestamp": 1710696600,
                "periods": {"first": 1710696600, "second": 1710700200},
                "venue": {"id": 1488, "name": "Estadio de Vallecas", "city": "Madrid"},
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 728,
                    "name": "Rayo Vallecano",
                    "logo": "https://media.api-sports.io/football/teams/728.png",
                    "winner": True,
                },
                "away": {
                    "id": 543,
                    "name": "Real Betis",
                    "logo": "https://media.api-sports.io/football/teams/543.png",
                    "winner": False,
                },
            },
            "goals": {"home": 2, "away": 0},
            "score": {
                "halftime": {"home": 1, "away": 0},
                "fulltime": {"home": 2, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038237,
                "referee": "Cesar Soto Grado, Spain",
                "timezone": "UTC",
                "date": "2024-03-15T20:00:00+00:00",
                "timestamp": 1710532800,
                "periods": {"first": 1710532800, "second": 1710536400},
                "venue": {
                    "id": 1491,
                    "name": "Reale Arena",
                    "city": "Donostia-San Sebastián",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 548,
                    "name": "Real Sociedad",
                    "logo": "https://media.api-sports.io/football/teams/548.png",
                    "winner": True,
                },
                "away": {
                    "id": 724,
                    "name": "Cadiz",
                    "logo": "https://media.api-sports.io/football/teams/724.png",
                    "winner": False,
                },
            },
            "goals": {"home": 2, "away": 0},
            "score": {
                "halftime": {"home": 1, "away": 0},
                "fulltime": {"home": 2, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038238,
                "referee": "Francisco Hernandez Maeso, Spain",
                "timezone": "UTC",
                "date": "2024-03-17T13:00:00+00:00",
                "timestamp": 1710680400,
                "periods": {"first": 1710680400, "second": 1710684000},
                "venue": {
                    "id": 1494,
                    "name": "Estadio Ramón Sánchez Pizjuán",
                    "city": "Sevilla",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 536,
                    "name": "Sevilla",
                    "logo": "https://media.api-sports.io/football/teams/536.png",
                    "winner": False,
                },
                "away": {
                    "id": 538,
                    "name": "Celta Vigo",
                    "logo": "https://media.api-sports.io/football/teams/538.png",
                    "winner": True,
                },
            },
            "goals": {"home": 1, "away": 2},
            "score": {
                "halftime": {"home": 1, "away": 0},
                "fulltime": {"home": 1, "away": 2},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038239,
                "referee": "Jorge Figueroa Vazquez, Spain",
                "timezone": "UTC",
                "date": "2024-03-17T15:15:00+00:00",
                "timestamp": 1710688500,
                "periods": {"first": 1710688500, "second": 1710692100},
                "venue": {
                    "id": 1498,
                    "name": "Estadio de la Cerámica",
                    "city": "Villarreal",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 533,
                    "name": "Villarreal",
                    "logo": "https://media.api-sports.io/football/teams/533.png",
                    "winner": True,
                },
                "away": {
                    "id": 532,
                    "name": "Valencia",
                    "logo": "https://media.api-sports.io/football/teams/532.png",
                    "winner": False,
                },
            },
            "goals": {"home": 1, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 1, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038240,
                "referee": "Ricardo De Burgos Bengoetxea, Spain",
                "timezone": "UTC",
                "date": "2024-03-16T13:00:00+00:00",
                "timestamp": 1710594000,
                "periods": {"first": 1710594000, "second": 1710597600},
                "venue": {
                    "id": 19940,
                    "name": "Estadi Mallorca Son Moix",
                    "city": "Palma de Mallorca",
                },
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 798,
                    "name": "Mallorca",
                    "logo": "https://media.api-sports.io/football/teams/798.png",
                    "winner": True,
                },
                "away": {
                    "id": 715,
                    "name": "Granada CF",
                    "logo": "https://media.api-sports.io/football/teams/715.png",
                    "winner": False,
                },
            },
            "goals": {"home": 1, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 1, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1038241,
                "referee": "Alejandro Muniz Ruiz, Spain",
                "timezone": "UTC",
                "date": "2024-03-16T20:00:00+00:00",
                "timestamp": 1710619200,
                "periods": {"first": 1710619200, "second": 1710622800},
                "venue": {"id": 1460, "name": "San Mamés Barria", "city": "Bilbao"},
                "status": {"long": "Match Finished", "short": "FT", "elapsed": 90},
            },
            "league": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain",
                "logo": "https://media.api-sports.io/football/leagues/140.png",
                "flag": "https://media.api-sports.io/flags/es.svg",
                "season": 2023,
                "round": "Regular Season - 29",
            },
            "teams": {
                "home": {
                    "id": 531,
                    "name": "Athletic Club",
                    "logo": "https://media.api-sports.io/football/teams/531.png",
                    "winner": True,
                },
                "away": {
                    "id": 542,
                    "name": "Alaves",
                    "logo": "https://media.api-sports.io/football/teams/542.png",
                    "winner": False,
                },
            },
            "goals": {"home": 2, "away": 0},
            "score": {
                "halftime": {"home": 2, "away": 0},
                "fulltime": {"home": 2, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
    ],
}
