from django.urls import path
from . import views
urlpatterns = [
    path("bot-setup/", views.bot_setup, name="bot-setup"),
]