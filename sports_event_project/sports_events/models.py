from django.db import models
from sports.models import Sport
from django.contrib.auth.models import User


class Sports_event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=100)
    competitiveness_level = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)


# Create your models here.
