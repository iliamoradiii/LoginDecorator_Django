from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .Validators import *

def Index(request):
    return render(request, "index.html")

class Login(View):
    def get(self, request):
        return render(request, "LoginPage.html")

    @FormValidation
    @UserValidation
    def post(self, request, is_valid, cookie_string, role):
        if is_valid:
            response = redirect("/admin-panel")
            response.set_cookie('user-auth', cookie_string, max_age=timedelta(weeks=1))
            return response
        else:
            return render(request, "LoginPage.html", {"hasError": False, "error": "", "hasValidationError": True, "validation_error": "invalid User ( user not found )"})



