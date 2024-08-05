from django.shortcuts import render

# Create your views here.

def bot_setup(request):
    return render(request, "bot/bot_setup.html")