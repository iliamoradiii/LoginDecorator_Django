from functools import wraps
from django.shortcuts import redirect
from MainApp.CookieGenerator import *
from Models.models import Users

# this decorator is useless, but you can use it to check if is user login
# def IsLogin(view_func):
#     @wraps(view_func)
#     def wrapper(self, request, *args, **kwargs):
#         try:
#             cookie = request.COOKIES.get("user-auth", None)
#             user_obj = Cookie.DecodeCookie(cookie)
#
#             c_username = user_obj["username"]
#             user_db = Users.objects.get(Username=c_username)
#
#             return view_func(self, request, user_db, user_obj, *args, **kwargs)
#         except:
#             return redirect("/login")

def IsAdmin(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            cookie = request.COOKIES.get("user-auth", None)
            user_obj = Cookie.DecodeCookie(cookie)

            c_username = user_obj["username"]
            user_db = Users.objects.get(Username=c_username, IsAdmin=True)

            # checking if secret keys are 10 characters to make sure cookie is not fake
            # Tip : it's better to set factors with your own idea to make sure its unic !
            validation_number = 10
            c_user_secret_key1_isvalid = True if len(user_obj["secretKey1"]) == validation_number else False
            c_user_secret_key2_isvalid = True if len(user_obj["secretKey2"]) == validation_number else False

            if c_user_secret_key1_isvalid and c_user_secret_key2_isvalid:
                return view_func(request, user_db, user_obj, *args, **kwargs)

            else:
                return redirect("/login")
        except:
            # Program comes here if : cookie is not set / user is fake / user is not admin
            print("is admin validation failed")
            return redirect("/login")

    return wrapper