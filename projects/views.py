from django.shortcuts import render
from .models import Project
from .forms import PostProjectForm

def home(request):
    posts = Project.objects.all()
    context = {'posts': posts}
    return render(request, 'projects/index.html', context)

def create_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        url = request.POST.get('url')

        print(name, description, image, url)
    form = PostProjectForm()
    context = {'form': form}
    return render(request, 'projects/create_post.html', context)