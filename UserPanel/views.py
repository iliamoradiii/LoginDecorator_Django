from django.shortcuts import render
from AdminPanel.Validators import IsLogin


@IsLogin
def UserPanelView(request, user_db, user_obj):
    return render(request, "UserPanel_Index.html", {"name": user_db.Name})
