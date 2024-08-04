from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        myuser = User.objects.create_user(username, password, confirm_password)
        myuser.email = username+"@mfp.com"
        myuser.save()
        messages.success(request, 'Your account has been created!')
        return redirect('users/new-user')
    return render(request, "users/signup.html")

def index(request):
    return render(request, "users/index.html")

def login_page(request):
    return render(request, "users/login.html")

