from django.shortcuts import render, redirect

def search(request):
    return render(request, 'temp.html')

def hello_world(request):
    return render(request, 'temp.html')