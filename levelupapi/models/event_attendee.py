from django.db import models
from .event import Event
from .gamer import Gamer 

class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Gamer, on_delete=models.CASCADE)