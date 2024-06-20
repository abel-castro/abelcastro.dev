# abelcastro.dev

Source code of [abelcastro.dev](https://abelcastro.dev).

Built with Django and created with [DDST](https://github.com/abel-castro/ddst).

My goal was to create a simple solution for blogging without using a CMS.
This blog only uses django core functionalities and the great Markdown editor
[martor](https://github.com/agusmakmun/django-markdown-editor).

## API

This project also provides a REST-API with following endpoints:

- `GET /api/posts/` - return all posts
- `GET /api/posts/<slug>` - return one post
- `GET /api/sports/standings/` - return the current standings and results of some of the most important football competitions in Europe

  ```json
    [
      {
        "name": "Premier League",
        "slug": "english_premier_league",
        "logo": "https://media-4.api-sports.io/football/leagues/39.png",
        "teams": [
          {
              "position": 1,
              "name": "Manchester City",
              "points": 27,
              "logo": "https://media-4.api-sports.io/football/teams/50.png"
          },
          ...
        ],
        "results": [
          {
            "matchday": 1,
            "team_1": "Tottenham Hotspur",
            "team_1_goals": 1,
            "team_2": "Arsenal",
            "team_2_goals": 2
          },
          ...
        ]
      },
      ...
    ]

  ```

- `GET /api/sports/results/` - return results for the last matchday of some of the most important football competitions in Europe
  ```json
  {
      "english_premier_league": [
        {
          "matchday": 1,
          "homeTeam": "Tottenham Hotspur",
          "homeScore": 1,
          "awayTeam": "Arsenal",
          "awayScore": 2
        },
        ...
      ],
      "spanish_la_liga": [...],
      "italian_seria_a": [...],
      "german_bundesliga": [...],
      "austrian_bundesliga": [...],
      "french_ligue_1": [...],
      "portuguese_primeira_liga": [...]
  }
  ```

## Development

- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: `docker-compose build `

- Run `docker-compose up` and go to http://0.0.0.0:8000
  to see your runserver.

## Other commands

- Pytest

```
docker-compose run --rm django pytest
```

- Run black

```
docker-compose run --rm django black .
```

- Manual get data from API-Football standings

```
docker-compose run --rm django /app/manage.py import_league_standings
```

## Credits

- https://github.com/testdrivenio/django-on-docker-letsencrypt (staging setup
  is not working)
- [Bootstrap 5 Cover Example](https://getbootstrap.com/docs/5.0/examples/cover/)
