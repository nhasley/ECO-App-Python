from django.urls import path
from . import views

urlpatterns = [
  path('', views.posts_index, name='posts'),
  path('profile/', views.profile, name='profile'),
  path('challenges/', views.challenges, name='challenges'),
  path('<int:post_id>/', views.posts_detail, name='detail'),
  path('create/', views.PostCreate.as_view(), name='posts_create'),
  path('<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
  path('<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
  path('accounts/signup', views.signup, name='signup'), 
  ]