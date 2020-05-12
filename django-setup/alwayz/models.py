from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
