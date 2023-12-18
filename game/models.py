from django.contrib.auth.models import User
from django.db import models

from werewolf.settings import GAME_STATE_CHOICES


class Game(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(User, blank=True)
    max_players = models.IntegerField(default=10)
    game_state = models.IntegerField(choices=GAME_STATE_CHOICES, default=0)
    game_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_admin')

    def __str__(self):
        return f'[{self.id}] {self.name} - {self.game_state}'


