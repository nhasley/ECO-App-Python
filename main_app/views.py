from django.shortcuts import render


# Define the home view
def home(request):
    return render(request, 'home.html')

def challenges(request):
    return render(request, 'challenges.html')

def profile(request):
    return render(request, 'profile.html')
