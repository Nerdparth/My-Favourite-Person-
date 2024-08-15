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
        if request.method=="POST":
        #  try:
            user=request.user
            # bot = ChatDescription.objects.get(user=request.user)
            try:
             bot = BotInforamtion.objects.get(user=user)
            except:
             bot = BotInforamtion.objects.filter(user = user).first()

            # image = request.FILES['image']
            # bot.image = image
            chat_file = request.POST.get('drop-area')
            description = request.POST.get('describe')
            bot.chat_file = chat_file
            bot.botdescription = description
            bot.save()
            messages.success(request,"Person setup successful...")
            return redirect("/")

            # .objects.save(user=user, botdescription= description, chat_file=chat_file )
        #  except:
        #     messages.error(request,"Something went wrong")
            

        return render(request, "bot/chat_setup.html")

