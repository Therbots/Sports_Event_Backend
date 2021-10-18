from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from comments.models import Comment

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="replys", on_delete=models.CASCADE)
# Create your models here.
