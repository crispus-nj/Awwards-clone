from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('get-projects/', views.get_projects, name='projects'),
    path('get-project/<int:pk>/', views.get_project, name="project"),
    path('profile/<int:pk>/',views.profile, name='profile'),
    path('register/', views.authentication, name='register'),
    path('users/', views.get_users, name='users')
]
