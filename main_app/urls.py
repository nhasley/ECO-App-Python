from django.urls import path
from . import views

urlpatterns = [
  path('', views.challenges_index, name='challenges'),
  path('profile/', views.profile, name='profile'),
  path('upload/<int:challenge_id>/', views.upload, name='upload'),
  path('profile/add_photo/', views.add_photo, name='add_photo'),
]