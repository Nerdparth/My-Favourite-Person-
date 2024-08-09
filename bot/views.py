from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import bot_information




# Create your views here.
def bot_setup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        uuid = request.POST.get('uuid')
        bot_information.objects.create(user=user, name=name, age=age, gender=gender, uuid=uuid)
        return redirect('chat_setup')
    else:
       return render(request, "bot/bot_setup.html")
    
def chat_setup(request):
    return render(request, "bot/chat_setup.html")