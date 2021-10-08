from django.db import models
from django.contrib.auth.models import User
from sports_events.models import Sports_event

class Attending_athlete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sports_event = models.ForeignKey(Sports_event, on_delete=models.CASCADE)

# Create your models here.
