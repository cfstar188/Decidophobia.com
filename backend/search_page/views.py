from django_nextjs.render import render_nextjs_page_sync
from django.shortcuts import render, redirect

def search(request):
    return render_nextjs_page_sync(request)

def hello_world(request):
    return render(request, 'temp.html')