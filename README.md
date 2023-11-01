# abelcastro.dev
Source code of [abelcastro.dev](https://abelcastro.dev). 

Built with Django and created with [DDST](https://github.com/abel-castro/ddst).

My goal was to create a simple solution for blogging without using a CMS.
This blog only uses django core functionalities and the great Markdown editor 
[martor](https://github.com/agusmakmun/django-markdown-editor).

## API
This project also provides a REST-API with following endpoints:

- `GET /api/posts/` - return all posts
- `GET /sports/standings/` - return the current standings of some of the most important football competitions in Europe


## Development
- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: ```docker-compose build ```

- Run ```docker-compose up``` and go to http://0.0.0.0:8000
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

## Credits
- https://github.com/testdrivenio/django-on-docker-letsencrypt (staging setup 
  is not working)
- [Bootstrap 5 Cover Example](https://getbootstrap.com/docs/5.0/examples/cover/)
