from django.urls import path
from . import views

urlpatterns = [
  path('', views.challenges_index, name='challenges'),
  path('profile/', views.profile, name='profile'),
]