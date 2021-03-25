# abelcastro.dev
Source code of [abelcastro.dev](https://abelcastro.dev). 

Built with Django and created with [DDST](https://github.com/abel-castro/ddst).

My goal was to create a simple solution for blogging without using a CMS.
This blog only uses django core functionalities and the great Markdown editor 
[martor](https://github.com/agusmakmun/django-markdown-editor).


### Development
- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: ```docker-compose build ```

- Run ```docker-compose up``` and go to http://0.0.0.0:8000
to see your runserver.


### Other commands
- Run black
```
docker-compose run --rm django black .
```

### Credits
- https://github.com/testdrivenio/django-on-docker-letsencrypt (staging setup 
  is not working)
- [Bootstrap 5 Cover Example](https://getbootstrap.com/docs/5.0/examples/cover/)
