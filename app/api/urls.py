from api.views import PostListAPI
from django.urls import path

app_name = "users"
urlpatterns = [
    path("posts/", view=PostListAPI.as_view(), name="post_list"),
]
