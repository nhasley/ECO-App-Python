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
    points = models.IntegerField(
        default=10
    )
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"