from django.contrib import admin
from player.models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display=('id','picture', 'name', 'team_name')

admin.site.register(Player, PlayerAdmin)
# Register your models here.