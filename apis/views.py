from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, UserSerializer, UserProfileSerializer
from projects.models import Project
from accounts.models import UserAccount

# Create your views here.
@api_view()
def get_routes(request):
    urls = [
        'GET api',
        'GET api/get-projects/',
        'GET api/get-project/<int:pk>/',
        'GET api/users/',
        'POST api/register/'
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

@api_view(['POST'])
def authentication(request):

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
def get_users(request):
    users = UserAccount.objects.all().order_by('-last_login')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def profile(request, pk):
    user = UserAccount.objects.get(id = pk)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserProfileSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)    