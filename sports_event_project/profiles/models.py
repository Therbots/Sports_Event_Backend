from django.db import models
from django.contrib.auth.models import User

def upload_path(instance, filename):
    return '/'.join(['image', str(instance.name), filename])

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()

# Create your models here.
