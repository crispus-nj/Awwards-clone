from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Project, Like
from .forms import PostProjectForm

def home(request):
    posts = Project.objects.all()
    user = request.user
    context = {'posts': posts, 'user': user}
    return render(request, 'projects/index.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project_link = form.cleaned_data['project_link']
            image = form.cleaned_data['image']

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
    
@login_required(login_url='login')
def like_post(request):
    user = request.user

    if request.method == 'POST':
        post_id = request.POST.get('post')
        post_obj = Project.objects.get(id = post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else :
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if created:
            if like.value == 'like':
                like.value == 'unlike'
            else :
                like.value == 'like'
            
        like.save()    
    return redirect('home')