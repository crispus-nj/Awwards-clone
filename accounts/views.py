from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import UserAccount
from .forms import RegisterForm
from projects.models import Project
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form)
        # print (type(form.errors))
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = UserAccount.objects.create_user(
                email = email,
                username = username,
                password = password
            )
            user.is_active = True
            user.save()
            # login(request, user)
            return redirect('login')
        else :
            print("form is invalid!") 
            
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            return HttpResponse("Invalid user")
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request, pk):
    user = UserAccount.objects.get(id=pk)
    posts = user.project_set.all()
    context = {'posts': posts, 'user': user}
    return render(request, 'accounts/profile.html', context)
