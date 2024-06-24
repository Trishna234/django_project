from django.urls import path
from base import views
urlpatterns = [
    path("create/", views.create_todo, name="create")
]