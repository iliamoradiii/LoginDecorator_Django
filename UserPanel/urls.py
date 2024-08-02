from django.urls import path, include
from UserPanel.views import *

urlpatterns = [
    path("", UserPanelView, name="adminPanel"),
]