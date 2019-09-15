from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Post 
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'codebloodedkillers'

# Define the home view
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})
def profile(request):
    return render(request, 'profile.html')