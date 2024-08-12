from django.shortcuts import render,redirect
from . models import BotInforamtion




# Create your views here.
def bot_setup(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        BotInforamtion.objects.create(user=user,name=name, age=age, gender=gender)
        return redirect('chat_setup')
    else:
       return render(request, "bot/bot_setup.html")
    
def chat_setup(request):

    if request.method=="POST":
        try:
            bot = BotInforamtion.objects.get(user=request.user)
            image = request.FILES['image']
            bot.image = image
            chat_file = request.FILES['chat_file']
            bot.save()

        except:
            pass

    return render(request, "bot/chat_setup.html")