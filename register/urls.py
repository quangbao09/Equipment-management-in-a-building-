from django.urls import path
from . import views

app_name = "register"
urlpatterns = [
    path("", views.registerUser.as_view(), name="registerUsser"),
]