from api.serializers import PostSerializer
from sports.get_leagues_data_from_db import get_current_standings_data
from basic_analytics_tracker.mixins import TrackingMixin
from blog.models import Post
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostListAPI(TrackingMixin, ListAPIView):
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    serializer_class = PostSerializer


class StandingsAPI(TrackingMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = get_current_standings_data()
        return Response(data, status=status.HTTP_200_OK)
