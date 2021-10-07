from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Sport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    competitiveness_level = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=100)

# Create your models here.
