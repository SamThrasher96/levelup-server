from django.db import models
from .gamer import Gamer
from .game import Game

class Event(models.Model):
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event_date = models.DateField(auto_now=False, auto_now_add=False)