from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
  path('', views.challenges, name='challenges'),
=======
  path('', views.home, name='home'),
  path('challenges/', views.challenges, name='challenges'),
>>>>>>> 306619085fa4c516c139ff243cd800d7118bd32c
  path('profile/', views.profile, name='profile'),
]