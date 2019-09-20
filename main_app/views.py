from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
import uuid
import boto3
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyD-GuHDc6HmxIMV3-AJsxuuPf63NdXqts0'

google_places = GooglePlaces(YOUR_API_KEY)

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'codebloodedkillers'

# Define the home view
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def profile(request):
    posts = Post.objects.all()
    return render(request, 'profile.html', {'posts': posts})

def challenges(request):
    return render(request, 'challenges.html')

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
    fields = ['photo', 'challenge', 'description', 'location']
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        query_result = google_places.text_search(query = form.instance.location)
        print(query_result.places[0].geo_location)
        form.instance.lat = query_result.places[0].geo_location.get('lat')
        form.instance.lng = query_result.places[0].geo_location.get('lng')
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['photo', 'challenge', 'description']
    success_url = '/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)