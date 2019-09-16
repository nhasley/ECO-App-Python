from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_index, name='posts'),
  path('profile/', views.profile, name='profile'),
  path('<int:post_id>/', views.posts_detail, name='detail'),
  path('create/', views.PostCreate.as_view(), name='posts_create'),
  path('<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
  path('<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
  path('<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
]