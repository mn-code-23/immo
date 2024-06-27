from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Agent

User = get_user_model()
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    return redirect('index')

def profil(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        user = request.user
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.username = username
        user.save()
        return redirect('index')
    return render(request, "profil.html")

def agent(request):
    agent = Agent.objects.all()
    return render(request, "agent.html", context={"agent": agent})