from django.urls import path
from . import views
urlpatterns = [
    path("bot-setup/", views.bot_setup, name="bot-setup"),
    path('chat-setup/', views.chat_setup, name='chat_setup')
]
