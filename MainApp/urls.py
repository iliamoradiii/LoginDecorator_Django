from django.urls import path
from . import views as Views

urlpatterns = [
    path("", Views.Index, name="HomePage"),
    path("login", Views.Login.as_view(), name="LoginPage"),
]