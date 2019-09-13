from django.shortcuts import render

class Challenge:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, points, description):
    self.name = name
    self.points = points
    self.description = description

challenges = [
  Challenge('Bike', 10, 'Take a pic'),
]

# Define the home view
def challenges_index(request):
    return render(request, 'challenges.html', {'challenges': challenges})

def profile(request):
    return render(request, 'profile.html')
