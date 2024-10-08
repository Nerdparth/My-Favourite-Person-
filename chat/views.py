from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from bot.models import BotInforamtion
# Create your views here.

def index(request):
    return JsonResponse({'message': 'Hello World!'})


def home(request):
    
    user = request.user
    bot = None
    if user.is_authenticated:
        try:
            bot  = BotInforamtion.objects.get(user=user)
        except:
            return redirect('/bot/bot-setup')    
    return render(request, "chat/home.html",context={"bot":bot})




# class Chat:
#     def __init__(self, user, timestamp,message):
#         self.user = user
#         self.timestamp = timestamp

#     def create_chat(self):
#         chat = Chat.objects.get_or_create(user=self.user)
#         return chat

# class ChatMessage:
#     def __init__(self, message, timestamp, is_user_message, chat, uuid):
#         self.message = message
#         self.timestamp = timestamp
#         self.is_user_message = is_user_message
#         self.chat = chat
#         self.uuid = uuid
    
#     def create_chat_message(self):
#         chat_message = ChatMessage.objects.create(message=self.message, is_user_message=self.is_user_message, chat=self.chat, uuid=self.uuid)
#         return chat_message

# def start_chat(request):
#     if request.method == 'POST':
#         user = request.user
#         message = request.POST['message']
#         userObj = User.objects.get(username=user)
#         chat = Chat.objects.get_or_create(user=userObj)
#         if(chat[1] == False):
#             chat = chat[0]
#         else:
#             chat = chat[0]
#         chat_message = ChatMessage.objects.create(message=message, is_user_message=True, chat=chat)
#         chat_message.save()
        
#         bot_message = ChatMessage.objects.create(message='Hello!', is_user_message=False, chat=chat)
#         bot_message.save()

#         return JsonResponse({'message': 'message sent'})
#     return JsonResponse({'message': 'Chat not started!'})


# class ChatBody:
#     def __init__(self, message,time_stamp, is_user_message):
#         self.message = message
#         self.time_stamp = time_stamp
#         self.is_user_message = is_user_message
    
#     def chat_json(self):
#         return {
#             'message': self.message,
#             'time_stamp': self.time_stamp,
#             'sender': "user" if self.is_user_message else "bot"
#         }


# def return_chat_messages(request):
#     if request.method == 'GET':
#         user = request.user
#         userObj = User.objects.get(username=user)
#         try:
#             chat = Chat.objects.get(user=userObj)
#             chat_messages = ChatMessage.objects.filter(chat=chat)
#             messages = []
#             for i in chat_messages:
#                 chat_body = ChatBody(i.message, i.timestamp, i.is_user_message)
#                 messages.append(chat_body.chat_json())
#             return JsonResponse({'chat_messages': messages})
#         except:
#             return JsonResponse({'message': 'Chat messages not returned!'})
#     return JsonResponse({'message': 'Chat messages not returned!'})

