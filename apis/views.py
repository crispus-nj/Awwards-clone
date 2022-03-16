from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from projects.models import Project

# Create your views here.
@api_view()
def get_routes(request):
    urls = [
        'GET '
    ]
    return Response(urls)

@api_view(['GET'])
def get_projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProductSerializer(projects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_project(request, pk):
    if request.method == 'GET':
        project = Project.objects.get(id = pk)
        serializer = ProductSerializer(project)
        return Response(serializer.data)

