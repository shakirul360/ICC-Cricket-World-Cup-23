from django.contrib import admin
from match.models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display=('match_no', 'match_team1', 'match_team2', 'match_date', 'match_highlights')

admin.site.register(Match, MatchAdmin)
# Register your models here.