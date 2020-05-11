from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.StringRelatedField()
    date = models.DateTimeField(default=timezone.now)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.name
