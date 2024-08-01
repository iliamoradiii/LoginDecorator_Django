from django.urls import path, include
from . import views as AdminViews

urlpatterns = [
    path("", AdminViews.AdminPanel_IndexPage, name="adminPanel"),
]