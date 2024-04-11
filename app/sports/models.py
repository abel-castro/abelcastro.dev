from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    logo = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    position = models.PositiveSmallIntegerField()
    points = models.SmallIntegerField()
    logo = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Result(models.Model):
    homeTeam = models.CharField(max_length=100)
    awayTeam = models.CharField(max_length=100)
    homeScore = models.PositiveSmallIntegerField()
    awayScore = models.PositiveSmallIntegerField()
    matchday = models.PositiveSmallIntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="results")

    def __str__(self) -> str:
        return f"{self.homeTeam} {self.homeScore} - {self.awayScore} {self.awayTeam} at matchday {self.matchday}"
