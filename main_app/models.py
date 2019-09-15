from django.db import models
from django.contrib.auth.models import User

CHALLENGES = (
    ('M', 'Metro'),
    ('B', 'Bike'),
    ('W', 'Walk')
)

class Post(models.Model):
    description = models.CharField(max_length=100) 
    challenge = models.CharField(
        max_length=10,
        choices=CHALLENGES,
        default=CHALLENGES[0][0]
    )

    def __str__(self):
        return self.name