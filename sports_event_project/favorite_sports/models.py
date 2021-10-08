from django.db import models
from django.contrib.auth.models import User
from sports.models import Sport

class Favorite_sport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    

# Create your models here.
