"""
USER ACCOUNT DJANGO TEMPLATE FROM THIS VIDEO: https://www.youtube.com/watch?v=Z3qTXmT0yoI
"""

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def hello_world(request):
    return render(request, 'temp.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login/")
    context = {'registrationform': form}
    return render(request, 'useraccounts/register.html', context)

def login(request):
    form = CreateLoginForm()
    if request.method == "POST":
        form = CreateLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard/")
    context = {"loginform": form}
    return Response({"message": "Login failed."}, status=status.HTTP_200_OK)

@login_required(login_url="login/")
def dashboard(request):
    return render(request, 'useraccounts/dashboard.html')

def logout(request):
    auth.logout(request)
    return render(request, 'useraccounts/logout.html')