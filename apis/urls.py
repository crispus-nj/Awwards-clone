from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('get-projects/', views.get_projects, name='projects'),
    path('get-project/<int:pk>', views.get_project, name="project")
]
