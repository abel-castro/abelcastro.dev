from blog.models import Post, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("title", "slug", "meta_description", "content", "date", "tags")


"""
Sports-dashboard
"""


class TeamSerializer(serializers.Serializer):
    position = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    points = serializers.IntegerField(read_only=True)
    logo = serializers.CharField(read_only=True)


class ResultSerializer(serializers.Serializer):
    position = serializers.IntegerField(read_only=True)
    team_1 = serializers.CharField(read_only=True)
    team_1_goals = serializers.IntegerField(read_only=True)
    team_2 = serializers.CharField(read_only=True)
    team_2_goals = serializers.IntegerField(read_only=True)


class LeagueSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    teams = serializers.ListField(child=TeamSerializer(), read_only=True)
    logo = serializers.CharField(read_only=True)
    results = serializers.ListField(child=ResultSerializer(), read_only=True)


class ResultsSerializer(serializers.Serializer):
    english_premier_league = serializers.ListField(
        child=ResultSerializer(), read_only=True
    )
    spanish_la_liga = serializers.ListField(child=ResultSerializer(), read_only=True)
    italian_seria_a = serializers.ListField(child=ResultSerializer(), read_only=True)
    german_bundesliga = serializers.ListField(child=ResultSerializer(), read_only=True)
    french_ligue_1 = serializers.ListField(child=ResultSerializer(), read_only=True)
    portuguese_primeira_liga = serializers.ListField(
        child=ResultSerializer(), read_only=True
    )


class LeaguesSerializer(serializers.Serializer):
    english_premier_league = serializers.ListField(
        child=LeagueSerializer(), read_only=True
    )
    spanish_la_liga = serializers.ListField(child=LeagueSerializer(), read_only=True)
    italian_seria_a = serializers.ListField(child=LeagueSerializer(), read_only=True)
    german_bundesliga = serializers.ListField(child=LeagueSerializer(), read_only=True)
    french_ligue_1 = serializers.ListField(child=LeagueSerializer(), read_only=True)
    portuguese_primeira_liga = serializers.ListField(
        child=LeagueSerializer(), read_only=True
    )
