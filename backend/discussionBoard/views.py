from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
from django.http import HttpResponse
<<<<<<< HEAD
from django.http import JsonResponse
=======
>>>>>>> main

# Create your views here.
def messageBoard(request):
    messages = []
    for i in models.Message.objects.all():
        messages.append(i)

<<<<<<< HEAD
=======
    context = {'messagesList' : messages}

>>>>>>> main
    if request.method == 'POST':
        if request.user.is_authenticated:
            req = request.POST.get('your_message')
            replyreq = request.POST.get('reply_message')
            replyingTo = request.POST.get('replyingTo')

            if req is not None:
                models.Message.objects.create(user=request.user, message=req)
            elif replyreq is not None:
                models.Message.objects.create(user=request.user, message=replyreq, replyTo=replyingTo)
            return redirect('http://127.0.0.1:8000/discussion_board/messages/')
        else:
            return redirect('http://127.0.0.1:8000/login/')

<<<<<<< HEAD
    response = JsonResponse({'messagesList' : messages})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
=======
    return render(request, 'discussBoard.html', context=context)
>>>>>>> main


def requestTest(request):
    return HttpResponse(request.body)

def htmlAndCssTest(request):
    return render(request, 'testo.html')