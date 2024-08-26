from api.examples import RESULTS_API_EXAMPLE, STANDINGS_API_EXAMPLE
from api.serializers import (LeaguesSerializer, PostSerializer,
                             ResultsSerializer)
from basic_analytics_tracker.mixins import TrackingMixin
from blog.models import Post
from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   extend_schema)
from rest_framework import status
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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="query",
            description="Filter posts by title, content, or tags. Use a search term to filter posts.",
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        ),
    ],
    responses={200: PostSerializer(many=True)},
)
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
    @extend_schema(
        description="Show the standings and results of every available league",
        responses={200: LeaguesSerializer},
        examples=[
            OpenApiExample(
                "200: success",
                value=STANDINGS_API_EXAMPLE,
                status_codes=["200"],
            )
        ],
    )
    def get(self, request, *args, **kwargs):
        data = get_current_standings_data()
        return Response(data, status=status.HTTP_200_OK)


class ResultsAPI(TrackingMixin, APIView):
    @extend_schema(
        description="Show the results and standings of every available league",
        responses={200: ResultsSerializer},
        examples=[
            OpenApiExample(
                "200: success",
                value=RESULTS_API_EXAMPLE,
                status_codes=["200"],
            )
        ],
    )
    def get(self, request, *args, **kwargs):
        data = get_current_results_data()
        return Response(data, status=status.HTTP_200_OK)
