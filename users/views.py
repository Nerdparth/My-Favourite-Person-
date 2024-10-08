from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password.strip() != "" or confirm_password.strip() !="": 
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, "users/signup.html")
        
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
                return render(request, "users/signup.html")
        
            # Create new user
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 

            messages.success(request, 'Your account has been created!')
            return redirect('/bot/bot-setup/')    
        else:
            messages.error(request, 'Password cannot be empty')

            return render(request, "users/signup.html")
        
        
    
    return render(request, "users/signup.html")

# def bot_setup(request):
#     if request.method == 'POST':
#         unique_id = request.session.get('unique_id')
#         if unique_id:
#             # Use BotInformation to store data
#             bot_information.objects.create(  age=request.POST['age'],
#                 name=request.POST['name'],
#                 gender=request.POST['gender']
#             )
              
            # del request.session['unique_id']  # Remove UUID from session
        # return redirect('home')
    
    # return render(request, 'bot_setup.html')

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
            return redirect('/')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request) # logout
    messages.success(request, 'You have been logged')
    return redirect('login-user')

