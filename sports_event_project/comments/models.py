from django.db import models
from django.contrib.auth.models import User
from event_message_boards.models import Event_message_board

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_message_board = models.ForeignKey(Event_message_board, on_delete=models.CASCADE)

# Create your models here.
