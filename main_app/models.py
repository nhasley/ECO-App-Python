from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
