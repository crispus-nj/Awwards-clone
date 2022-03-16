from  django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('create-post/', views.create_post, name='create-post'),
    path('like-post/', views.like_post, name='like'),
    path('submit-review/<int:pk>/', views.submit_review ,name='ratings')
]

