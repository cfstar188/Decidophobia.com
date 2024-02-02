from django.shortcuts import render

def hello_world(request):
    # Could pass in a context into render to create 
    # dynamic webpage
    return render(request, 'temp.html')