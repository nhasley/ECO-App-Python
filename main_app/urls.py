from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_index, name='posts'),
  path('profile/', views.profile, name='profile'),
]