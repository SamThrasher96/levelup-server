from django.db import models
from .event import Event
from .gamer import Gamer 

class EventAttendee(models.Model):
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendeeId = models.ForeignKey(Gamer, on_delete=models.CASCADE)