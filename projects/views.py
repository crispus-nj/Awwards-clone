from django.shortcuts import redirect, render
from .models import Project
from .forms import PostProjectForm

def home(request):
    posts = Project.objects.all()
    context = {'posts': posts}
    return render(request, 'projects/index.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project_link = form.cleaned_data['project_link']
            image = form.cleaned_data['image']
            print(name, description, project_link, image)
            project = Project.objects.create(
                name = name,
                author = request.user,
                description = description,
                project_link = project_link,
                image = image
            )
            return redirect('home')

    form = PostProjectForm()
    context = {'form': form}
    return render(request, 'projects/create_post.html', context)