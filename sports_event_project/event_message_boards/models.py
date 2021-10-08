from django.db import models
from sports_events.models import Sports_event

class Event_message_board(models.Model):
    sports_event = models.ForeignKey(Sports_event, on_delete=models.CASCADE)

# Create your models here.
