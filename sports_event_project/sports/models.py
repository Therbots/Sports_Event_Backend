from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Sport(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
