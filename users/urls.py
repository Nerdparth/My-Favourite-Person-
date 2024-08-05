from django.urls import path
from . import views
urlpatterns = [
    path("login-user/", views.login_view, name="login-user"),
    path("logout/", views.logout_view, name="logout-user"),

    path("index/", views.index, name="index"),
    path("new-user/", views.signup, name="signup")
]