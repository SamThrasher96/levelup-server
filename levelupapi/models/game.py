from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=250, default="Default Title")
    game_type_id = models.ForeignKey(GameType, on_delete=models.CASCADE)
    creator_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)