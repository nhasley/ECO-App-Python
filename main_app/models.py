from django.db import models
from django.contrib.auth.models import User

CHALLENGES = (
    ('Metro', 'Metro'),
    ('Bike', 'Bike'),
    ('Walk', 'Walk')
)

class Post(models.Model):
    challenge = models.CharField(
        max_length=10,
        choices=CHALLENGES,
        default='Metro'
    )
    description = models.CharField(max_length=100)