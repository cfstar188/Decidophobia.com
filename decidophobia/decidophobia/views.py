from django.shortcuts import render

def hello_world(request):
    return render(request, 'temp.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')