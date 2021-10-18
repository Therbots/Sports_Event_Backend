from django.db import models
from django.contrib.auth.models import User
from sports.models import Sport

class Skill_level(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport,  related_name="skill_levels",on_delete=models.CASCADE)
    level = models.CharField(max_length=100)

# Create your models here.
