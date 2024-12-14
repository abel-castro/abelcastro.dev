import graphene
from blog.models import Post, Tag
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
        title=graphene.String(),
        tags=graphene.List(graphene.String),
        content=graphene.String(),
    )
    post = graphene.Field(PostType, slug=graphene.String(required=True))

    def resolve_posts(
        root,
        info,
        title: str = None,
        slug: str = None,
        tags: str = None,
        content: str = None,
    ):
        queryset = Post.objects.filter(published=True).prefetch_related("tags")

        if title:
            queryset = queryset.filter(title__icontains=title)

        if slug:
            queryset = queryset.filter(slug__icontains=slug)

        if tags:
            queryset = queryset.filter(tags__name__in=tags).distinct()

        if content:
            queryset = queryset.filter(content__icontains=content)

        return queryset

    def resolve_post(root, info, slug: str):
        return Post.objects.get(slug=slug, published=True)


# Combine queries and mutations into a schema
schema = graphene.Schema(query=Query)
