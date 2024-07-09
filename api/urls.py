from django.urls import path

from api.views import TodoApiView

urlpatterns = [
    path("todo/", TodoApiView.as_view(), name="create"),
    path("todo/<int:pk>/", TodoApiView.as_view(), name="update"),

]
