from api.serializers import PostSerializer
from basic_analytics_tracker.mixins import TrackingMixin
from blog.models import Post
from rest_framework import status
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from sports.get_current_results_data_from_db import get_current_results_data
from sports.get_leagues_data_from_db import get_current_standings_data


class PostPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 100


class PostListAPI(TrackingMixin, ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        # filter posts by title, content or tags
        queryset = Post.objects.filter(published=True).prefetch_related("tags")
        query = self.request.query_params.get("query")
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query)
                | Q(title__icontains=query)
                | Q(tags__name=query)
            ).distinct()
        return queryset


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
