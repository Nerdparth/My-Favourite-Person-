from django.shortcuts import render,redirect
from . models import BotInforamtion,ChatDescription
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned




# Create your views here.
def bot_setup(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
     try:
        print(request.body)
        user = request.user
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        if BotInforamtion.objects.filter(user = user):
           messages.info(request, "please login, bot information already exists...")
           return redirect("/user/loin-user")
        BotInforamtion.objects.create(user=user,name=name, age=age, gender=gender)
        return redirect('/bot/chat-setup')
     except:
        if age == "" or name== "" or gender == "":
           messages.error(request, "fields cannot be empty")
           return redirect('/bot/bot-setup')
    return render(request, "bot/bot_setup.html")
      
    
    
def chat_setup(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        user = request.user
        try:
            bot = BotInforamtion.objects.get(user=user)
        except BotInforamtion.DoesNotExist:
            messages.error(request, "Bot information not found")
            return redirect('/bot/bot-setup')
        
        chat_file = request.FILES['chat_file']
        description = request.POST.get('describe')
        bot.botdescription = description
        
        try:
            # Read chat_file and convert to text
            chat_text = chat_file.read().decode('utf-8')
            bot.chat_file = f"you have to read the chat file and make sure to behave like the same person, just analyse every small detail how that person talks, how he behaves, remember the sole purpose is to not do anything cruel or offensive. Your are {bot.name} in the given chat and i am {user.username}. Gender is {bot.gender} and age is {bot.age} Here is the chat"+ chat_text
        except Exception as e:
            print(e)
            messages.error(request, "Error reading chat file")
            return redirect('/bot/chat-setup')
        
        bot.save()
        messages.success(request, "Person setup successful...")
        return redirect("/")
    
    return render(request, "bot/chat_setup.html")


