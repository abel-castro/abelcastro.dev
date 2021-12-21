from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return f"/{obj.slug}"


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return ["about_me"]

    def location(self, item):
        return reverse(item)
