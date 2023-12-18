from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from game.models import Game


class GameView(View):
    def get(self, request, id):
        try:
            game = Game.objects.get(id=id)

            # player must be admin or in the players
            if request.user != game.game_admin and request.user not in game.players.all():
                messages.error(request, "You do not have permission")
                return redirect('/')

        except Game.DoesNotExist:
            messages.error(request, "Game does not exists")
            return redirect('/')

        return render(request, 'game/index.html', {'game': game})


class NewGameView(View):
    def get(self, request):
        return render(request, 'game/new.html')

    def post(self, request):
        # check if user is admin in active game
        admin_count = Game.objects.filter(game_admin=request.user, game_state__gt=0).count()
        game_count = Game.objects.filter(players=request.user, game_state__gt=0).count()

        if admin_count > 0 or game_count > 0:
            messages.error(request, "Already in a game")
            return redirect('/')
        name = request.POST.get('name')
        max_players = request.POST.get('max')

        # todo check for name and max is number
        game = Game.objects.create(name=name, max_players=max_players, game_admin=request.user)
        return redirect(f'/game/{game.id}/')


