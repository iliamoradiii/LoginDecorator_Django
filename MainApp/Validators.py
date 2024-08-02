from django.shortcuts import render, redirect
from functools import wraps

from Models.models import Users
from MainApp.CookieGenerator import Cookie

def FormValidation(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        inp_list = [
            request.POST.get('username', ''),
            request.POST.get('password', '')
        ]
        _validInputLength = 3
        for inp in inp_list:
            if not inp or len(inp) < _validInputLength:
                return render(request, "LoginPage.html", {"hasError": True, "error": "input should not be empty !", "hasValidationError": False, "validation_error": ""})

        return view_func(self, request, *args, **kwargs)
    return wrapper

def UserValidation(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cookie_string = ""
        role = ""
        is_valid = False

        try:
            user = Users.objects.get(Username=username, Password=password)
            role = "SimpleUser"
            if user.IsAdmin:
                role = "AdminUser"

            cookie_string = Cookie.Generate(user.Username, role)
            is_valid = True
            return view_func(self, request, is_valid, cookie_string, role, *args, **kwargs)

        except:
            is_valid = False
            return view_func(self, request, is_valid, cookie_string, role, *args, **kwargs)

    return wrapper

def PreventRenderToLoginUser(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        try:
            cookie = request.COOKIES.get("user-auth")
            user_obj = Cookie.DecodeCookie(cookie)
            c_username = user_obj["username"]
            c_role = user_obj["role"]

            is_admin = False

            if c_role == "AdminUser":
                is_admin = True

            user_db = Users.objects.get(Username=c_username, IsAdmin=is_admin)

            if is_admin:
                return redirect("/admin-panel")
            else:
                return redirect("/user-panel")

        except:
            return view_func(self, request, *args, **kwargs)

    return wrapper
