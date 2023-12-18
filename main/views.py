from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from game.models import Game


class MainView(View):
    def get(self, request):
        games = []
        current = []
        if request.user.is_authenticated:
            games = Game.objects.filter(game_state=0)

        return render(request, 'main/index.html', {'games': games, 'current': current})
