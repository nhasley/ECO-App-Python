from django.shortcuts import render


# Define the home view
def challenges(request):
    return render(request, 'challenges.html', {'challenges': challenges})

def profile(request):
    return render(request, 'profile.html')
