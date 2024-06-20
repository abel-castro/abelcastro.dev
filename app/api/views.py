from api.serializers import PostSerializer
from basic_analytics_tracker.mixins import TrackingMixin
from blog.models import Post
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from sports.get_current_results_data_from_db import get_current_results_data
from sports.get_leagues_data_from_db import get_current_standings_data


class PostListAPI(TrackingMixin, ListAPIView):
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    serializer_class = PostSerializer

class PostDetailAPI(TrackingMixin, RetrieveAPIView):
    queryset = Post.objects.filter(published=True).prefetch_related("tags")
    serializer_class = PostSerializer
    lookup_field = "slug"

class StandingsAPI(TrackingMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = get_current_standings_data()
        return Response(data, status=status.HTTP_200_OK)


class ResultsAPI(TrackingMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = get_current_results_data()
        return Response(data, status=status.HTTP_200_OK)
