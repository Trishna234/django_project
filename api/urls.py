from django.urls import path

from api.views import TodoApiView

urlpatterns = [
    path("create_todo/", TodoApiView.as_view(), name="create")

]
