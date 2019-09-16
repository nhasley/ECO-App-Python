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
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return render(request, 'posts/detail.html', {'post':post})

class PostCreate(CreateView):
    model = Post
    fields = ['photo', 'challenge', 'description']
    success_url = '/'

class PostUpdate(UpdateView):
    model = Post
    fields = ['photo', 'challenge', 'description']
    success_url = '/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/'