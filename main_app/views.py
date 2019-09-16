from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post':post})

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/'

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/'

class PostDelete(DeleteView):
  model = Post
  success_url = '/'