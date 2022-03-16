from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Project, Like, RatingReview
from .forms import PostProjectForm, ReviewForm

def home(request):
    posts = Project.objects.all().order_by('-date_posted')
    user = request.user
    context = {'posts': posts, 'user': user}
    return render(request, 'projects/index.html', context)

def posts(request):
    posts = Project.objects.all().order_by('-date_posted')
    context = {'posts': posts}
    return render(request, 'projects/posts.html', context)

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
            return redirect('posts')

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
    return redirect('posts')

@login_required(login_url='login')
def submit_review(request, pk):

    url =  request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        try:
            reviews = RatingReview.objects.get(user__id = request.user.id, project__id= pk)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            
            return redirect(url)

        except RatingReview.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = RatingReview()
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.project_id = pk
                data.user_id = request.user.id
                data.save()

                return redirect(url)
            