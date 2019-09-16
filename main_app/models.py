from django.db import models
from django.contrib.auth.models import User

CHALLENGES = (
    ('Metro', 'Metro'),
    ('Bike', 'Bike'),
    ('Walk', 'Walk')
)

class Post(models.Model):
    photo = models.CharField(max_length=500)
    challenge = models.CharField(
        max_length=10,
        choices=CHALLENGES,
        default='Metro'
    )
    description = models.CharField(max_length=100)
    points = models.IntegerField(
        default=10
    )