from django.db import models
from django.db.models.fields import CharField
from sports_events.models import Sports_event

class Event_message_board(models.Model):
    sports_event = models.ForeignKey(Sports_event, related_name="event_message_boards", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

# Create your models here.
