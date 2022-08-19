from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(req):
    return HttpResponse("This is home page")


def dashboard(req):
    return HttpResponse("this is account dashboard")


def log_in(req):
    if req.user and req.user.is_authenticated:
        return redirect("/account/profile")
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect("/account/profile")
    return render(req, "account/index.html")


def register(req):
    if req.user and req.user.is_authenticated:
        return redirect("/account/profile")
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        email = req.POST.get("email", False)
        if username and password and email:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("/account/profile")
    return render(req, "account/index.html")


def log_out(req):
    if User and User.is_authenticated:
        logout(req)
        return redirect("/account/")
    return redirect("/login")


def profile(req):
    return HttpResponse("this is your profile")
