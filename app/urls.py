"""abelcastrodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from blog.sitemaps import PostSitemap, StaticSitemap
from blog.views import (
    AboutMeView,
    PostsListView,
    PostDetailView,
    PostsLoadMoreView,
    PostSearchView,
)


sitemaps = {"posts": PostSitemap, "static": StaticSitemap}

urlpatterns = [
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("martor/", include("martor.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("", cache_page(60 * 60)(PostsListView.as_view()), name="post_list"),
    path("search/", PostSearchView.as_view(), name="search"),
    path("more-posts/", PostsLoadMoreView.as_view(), name="more_posts"),
    path("about-me/", cache_page(60 * 60)(AboutMeView.as_view()), name="about_me"),
    path(
        "<slug:slug>/",
        cache_page(60 * 60)(PostDetailView.as_view()),
        name="post_detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
