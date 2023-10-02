from api.serializers import PostSerializer
from basic_analytics_tracker.mixins import TrackingMixin
from blog.models import Post
from django.shortcuts import render
from rest_framework.generics import ListAPIView


class PostListAPI(TrackingMixin, ListAPIView):
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    serializer_class = PostSerializer
