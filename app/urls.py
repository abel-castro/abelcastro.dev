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

from blog.sitemaps import StaticSitemap
from blog.views import (HomeView, PrivacyPolicyView, RedirectToNewBlogPostView,
                        RedirectToNewBlogView, robots_txt)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.decorators.cache import cache_page
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

sitemaps = {"static": StaticSitemap}

urlpatterns = [
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("martor/", include("martor.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # API docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    # API
    path("api/", include("api.urls", namespace="api")),
    # Home
    path("", cache_page(60 * 60)(HomeView.as_view()), name="home"),
    # Blog (redirect to new blog.abelcastro.dev)
    # path("blog/search/", PostSearchView.as_view(), name="search"),
    # path("blog/more-posts/", PostsLoadMoreView.as_view(), name="more_posts"),
    path(
        "privacy-policy/",
        cache_page(60 * 60)(PrivacyPolicyView.as_view()),
        name="privacy_policy",
    ),
    path("robots.txt", robots_txt),
    path(
        "blog",
        RedirectToNewBlogView.as_view(),
        name="redirect_to_new_blog",
    ),
    path(
        "<slug:slug>/",
        RedirectToNewBlogPostView.as_view(),
        name="redirect_to_new_blog",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
