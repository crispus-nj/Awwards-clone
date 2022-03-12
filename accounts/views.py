from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else: 
            return HttpResponse("Invalid user")
    return render(request, 'accounts/login.html')

def register(request):

    return render(request, 'accounts/register.html')