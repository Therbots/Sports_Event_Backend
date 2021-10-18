from django.db import models
from django.contrib.auth.models import User
from sports.models import Sport
from django.db.models.fields.related import ForeignKey

class Competitiveness_level(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, related_name="competitiveness_levels",on_delete=models.CASCADE)
    level = models.CharField(max_length=100)

# Create your models here.
