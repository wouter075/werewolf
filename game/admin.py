from django.contrib import admin

from game.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "current_players", "max_players", "game_state"]

    def current_players(self, obj):
        return obj.players.count()


admin.site.register(Game, GameAdmin)
