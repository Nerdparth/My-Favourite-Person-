from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="home"),
    # path("send-message/", views.start_chat, name="send-message"),
    # path("get-messages/", views.return_chat_messages, name="get-messages"),
]