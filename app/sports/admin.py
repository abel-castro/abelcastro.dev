from django.contrib import admin
from sports.models import League, Result, Team


class LeagueModelAdmin(admin.ModelAdmin):
    readonly_fields = ("updated_at",)


admin.site.register(League, LeagueModelAdmin)
admin.site.register(Team)
admin.site.register(Result)
