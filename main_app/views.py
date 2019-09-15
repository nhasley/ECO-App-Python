from django.shortcuts import render
from .models import Challenge

# Define the home view
def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges.html', {'challenges': challenges})

def profile(request):
    return render(request, 'profile.html')
