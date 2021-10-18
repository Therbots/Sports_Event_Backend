from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

# Create your models here.
