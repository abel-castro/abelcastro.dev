import graphene
from blog.models import Post, Tag
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from sports.get_leagues_data_from_db import get_current_standings_data
from sports.models import League, Result, Team

"""
Sports Types
"""


class LeagueType(DjangoObjectType):
    class Meta:
        model = League
        fields = ("id", "name", "slug", "logo", "updated_at", "teams", "results")


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "league", "position", "points", "logo")


class ResultType(DjangoObjectType):
    class Meta:
        model = Result
        fields = (
            "id",
            "homeTeam",
            "awayTeam",
            "homeScore",
            "awayScore",
            "matchday",
            "league",
        )


class TeamExternalEntity(graphene.ObjectType):
    name = graphene.String(required=True)
    position = graphene.Int()
    points = graphene.Int()
    logo = graphene.String()


# Subclass: TeamInternalEntity
class TeamInternalEntity(TeamExternalEntity):
    id = graphene.Int()
    data_provider_id = graphene.Int()


# ResultExternalEntity
class ResultExternalEntity(graphene.ObjectType):
    homeTeam = graphene.String()
    awayTeam = graphene.String()
    homeScore = graphene.Int()
    awayScore = graphene.Int()
    matchday = graphene.Int()


# LeagueExternalEntity
class LeagueExternalEntity(graphene.ObjectType):
    name = graphene.String(required=True)
    slug = graphene.String(required=True)
    teams = graphene.List(TeamExternalEntity)
    logo = graphene.String()
    results = graphene.List(ResultExternalEntity)


"""
Blog types
"""


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("title", "slug", "meta_description", "content", "date", "tags")


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ("name",)


class Query(graphene.ObjectType):
    ##########
    # Sports #
    ##########

    # Queries for League
    all_leagues = graphene.List(LeagueType)
    league_by_slug = graphene.Field(LeagueType, slug=graphene.String(required=True))

    # Queries for Team
    all_teams = graphene.List(TeamType)
    teams_by_league = graphene.List(
        TeamType, league_slug=graphene.String(required=True)
    )

    # Queries for Result
    all_results = graphene.List(ResultType)
    results_by_league = graphene.List(
        ResultType, league_slug=graphene.String(required=True)
    )
    results_by_matchday = graphene.List(
        ResultType, matchday=graphene.Int(required=True)
    )

    # Queries for Standings
    standings = graphene.List(LeagueExternalEntity)

    # Resolvers
    def resolve_all_leagues(root, info):
        return League.objects.all()

    def resolve_league_by_slug(root, info, slug):
        return League.objects.get(slug=slug)

    def resolve_all_teams(root, info):
        return Team.objects.all()

    def resolve_teams_by_league(root, info, league_slug):
        return Team.objects.filter(league__slug=league_slug)

    def resolve_all_results(root, info):
        return Result.objects.all()

    def resolve_results_by_league(root, info, league_slug):
        return Result.objects.filter(league__slug=league_slug)

    def resolve_results_by_matchday(root, info, matchday):
        return Result.objects.filter(matchday=matchday)

    def resolve_standings(root, info):
        return get_current_standings_data()

    ########
    # Blog #
    ########
    posts = graphene.List(
        PostType,
        search=graphene.String(required=False),
        limit=graphene.Int(default_value=3),
        offset=graphene.Int(default_value=0),
    )
    total_posts = graphene.Int(search=graphene.String(required=False))
    post = graphene.Field(PostType, slug=graphene.String(required=True))

    def resolve_posts(root, info, search: str = None, limit: int = 3, offset: int = 0):
        queryset = Post.objects.filter(published=True).prefetch_related("tags")

        if search is not None:
            queryset = queryset.filter(
                Q(content__icontains=search)
                | Q(title__icontains=search)
                | Q(tags__name=search)
            ).distinct()
        return queryset[offset : offset + limit]

    def resolve_total_posts(self, info, search=None):
        queryset = Post.objects.filter(published=True).prefetch_related("tags")

        if search is not None:
            queryset = queryset.filter(
                Q(content__icontains=search)
                | Q(title__icontains=search)
                | Q(tags__name=search)
            ).distinct()
        return queryset.count()

    def resolve_post(root, info, slug: str):
        return Post.objects.get(slug=slug, published=True)


# Combine queries and mutations into a schema
schema = graphene.Schema(query=Query)
