from django.urls import path
from base import views

urlpatterns = [
    path("create/", views.create_todo, name="create"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logout, name="logout")
]
