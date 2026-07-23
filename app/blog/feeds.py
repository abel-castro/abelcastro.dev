import datetime

from blog.constants import BLOG_DOMAIN, BLOG_META_DESCRIPTION, BLOG_TITLE
from blog.models import Post
from django.contrib.syndication.views import Feed
from django.utils import timezone
from martor.utils import markdownify


class LatestPostsFeed(Feed):
    title = BLOG_TITLE
    description = BLOG_META_DESCRIPTION
    author_name = "Abel Castro"
    link = f"{BLOG_DOMAIN}/"

    def items(self):
        return Post.objects.filter(published=True).prefetch_related("tags")[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdownify(item.content)

    def item_link(self, item):
        return f"{BLOG_DOMAIN}/{item.slug}/"

    def item_pubdate(self, item):
        if not item.date:
            return None
        return timezone.make_aware(
            datetime.datetime.combine(item.date, datetime.time.min)
        )

    def item_categories(self, item):
        return [tag.name for tag in item.tags.all()]
