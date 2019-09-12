from django.shortcuts import render

<<<<<<< HEAD
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Test</h1>')
=======
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Test<h1>')
>>>>>>> 128992a7e198d35a15491c8234332433e94f1c91
