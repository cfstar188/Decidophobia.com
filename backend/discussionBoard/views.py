from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
from django.http import HttpResponse

# Create your views here.
def messageBoard(request):
    messages = []
    for i in models.Message.objects.all():
        messages.append(i)

    context = {'messagesList' : messages}

    return render(request, 'discussBoard.html', context=context)


def requestTest(request):
    return HttpResponse(request.body)