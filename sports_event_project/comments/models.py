from django.db import models
from django.contrib.auth.models import User
from event_message_boards.models import Event_message_board

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    event_message_board = models.ForeignKey(Event_message_board, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.event_message_board.title, self.name)

# Create your models here.
