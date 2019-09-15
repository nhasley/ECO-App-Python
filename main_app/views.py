from django.shortcuts import render, redirect
from .models import Challenge, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'codebloodedkillers'

# Define the home view
def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges.html', {'challenges': challenges})

def profile(request):
    return render(request, 'profile.html')

def upload(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    return render(request, 'upload.html', {'challenge': challenge})

def add_photo(request, challenge_id): ##change to user
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, challenge_id=challenge_id) ##change to user
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('profile')