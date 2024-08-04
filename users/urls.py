from django.urls import path
from . import views
urlpatterns = [
    path("login-user/", views.login_page, name="login-user"),
    path("index/", views.index, name="index"),
    path("new-user/", views.signup, name="signup")
]