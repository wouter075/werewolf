import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from game.models import Game, Round


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
        admin_count = Game.objects.filter(game_admin=request.user).exclude(game_state=2).count()

        # check if user is in any active game
        game_count = Game.objects.filter(players=request.user).exclude(game_state=2).count()

        if admin_count > 0 or game_count > 0:
            messages.error(request, "Already in a game")
            return redirect('/')
        name = request.POST.get('name')
        max_players = request.POST.get('max')

        # check for null
        if len(name) == 0 or not max_players.isnumeric():
            messages.error(request, "Please enter a name and/or a valid number")
            return redirect('/')

        game = Game.objects.create(name=name, max_players=max_players, game_admin=request.user)
        return redirect(f'/game/{game.id}/')


class GameStart(View):
    def get(self, request, id):
        game = Game.objects.get(id=id)
        user_count = game.players.count()
        if user_count < 3:
            messages.error(request, "Not enough players")
            return redirect(request, f'/game/{game.id}/')

        user_ids = list(Game.objects.get(id=id).players.all().values_list('id', flat=True))
        random.shuffle(user_ids)

        # add a new round
        round = Round.objects.create(game=game)

        # set all to game_role 1
        for user_id in user_ids:
            user = User.objects.get(id=user_id)
            user.profile.game_role = 0
            user.save()

        # user_count > 3 < 7
        # 1 werewolf
        if 3 <= user_count < 7:
            # werewolf
            user = User.objects.get(id=user_ids[0])
            user.profile.game_role = 1
            user.save()

            # todo: save to round object
            # save: werewolf

            # save: civilian

        # set the game to started:
        game.game_state = 1
        game.save()


        return redirect(f'/game/{game.id}/')
