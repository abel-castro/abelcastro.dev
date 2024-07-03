from blog.models import Post
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return f"/blog/{obj.slug}"


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse(item)
