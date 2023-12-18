from django.contrib import admin

from game.models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "current_players", "max_players", "game_state"]

    def current_players(self, obj):
        return obj.players.count()


class RoundAdmin(admin.ModelAdmin):
    list_display = ["game", "round"]


admin.site.register(Game, GameAdmin)
admin.site.register(Round, RoundAdmin)
