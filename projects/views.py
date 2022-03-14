from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    posts = Project.objects.all()

    context = {'posts': posts}
    return render(request, 'projects/index.html', context)
    