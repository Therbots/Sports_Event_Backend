from django.db import models
from sports.models import Sport


class Sports_event(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=100)
    competitiveness_level = models.CharField(max_length=100)


# Create your models here.
