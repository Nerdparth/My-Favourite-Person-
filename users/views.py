from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
           messages.error(request, 'passwords do not match')
           return render(request, "users/signup.html")
        elif User.objects.filter(username=username).exists():
           messages.error(request, "username already exists please choose a different one")
        else:
           myuser = User.objects.create_user(username, password, confirm_password)
           myuser.email = username+"@mfp.com"
           myuser.save()
           messages.success(request, 'Your account has been created!')
           user = authenticate(request, username=username, password=password)
           login(request, user)
           return redirect('/bot/bot-setup/')
    return render(request, "users/signup.html")

def index(request):
    return render(request, "users/index.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login here
            messages.success(request, 'You have been logged')
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')



def logout_view(request):
    logout(request) # logout
    messages.success(request, 'You have been logged')
    return redirect('login-user')

