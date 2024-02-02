from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def questionnaire(request):
    if request.method == 'POST':
        priceFactor = request.POST.get("priceFactor")
        customerReview = request.POST.get("customerReview")
        shipping = request.POST.get("shipping")
        returnPolicy = request.POST.get("returnPolicy")
        brandReputation = request.POST.get("brandReputation")
        #contact with database to get selected information based on simple algorithm
        #how to return information to the search result page?