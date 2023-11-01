from api.views import PostListAPI, StandingsAPI
from django.urls import path
from django.views.decorators.cache import cache_page


app_name = "api"

urlpatterns = [
    path("posts/", view=cache_page(60 * 60)(PostListAPI.as_view()), name="post_list"),
    path(
        "sports/standings/",
        view=cache_page(60 * 60)(StandingsAPI.as_view()),
        name="get_standings",
    ),
]
