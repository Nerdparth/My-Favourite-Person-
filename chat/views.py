from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({'message': 'Hello World!'})

def home(request):
    return render(request, "chat/home.html")