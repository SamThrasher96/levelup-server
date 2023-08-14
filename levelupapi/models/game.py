from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=250, default="Default Title")
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    creator = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    players_needed = models.PositiveIntegerField(default=0)
    skill_level= models.CharField(max_length=250, default="easy")