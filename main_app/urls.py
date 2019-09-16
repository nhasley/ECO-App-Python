from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_index, name='posts'),
  path('profile/', views.profile, name='profile'),
  path('<int:post_id>/', views.posts_detail, name='detail'),
  path('create/', views.PostCreate.as_view(), name='posts_create'),
]