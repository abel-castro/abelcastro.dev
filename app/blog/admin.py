from django.contrib import admin

from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "content", "tags__name"]
    list_filter = ["published", "tags", "date"]


admin.site.register(Tag)
