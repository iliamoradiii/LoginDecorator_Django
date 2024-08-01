from django.shortcuts import render
from AdminPanel.Validators import IsAdmin


@IsAdmin
def AdminPanel_IndexPage(request, user_db, user_obj):
    return render(request, "AdminPanel_index.html", {"name": user_db.Name})
