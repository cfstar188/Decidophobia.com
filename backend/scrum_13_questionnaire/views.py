from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


from enum import Enum

class product(Enum):
    itemName = 0
    itemLink = 1
    itemImg = 2
    itemPrice = 3
    sellerScore = 4
    sellerPercentage = 5

# Create your views here.
def questionnaire(request):
    
    # So your questionnaire could call my function, and then I would search 
    # all available e-commerce sites with the inputted item name. then I would
    # return a list of items matching the item name, and then your file which 
    # has a questionnaire would use my returned list of items along with the 
    # inputted user preferences to rank each product and give it a the score 
    # out of 100
    # We can design the algorithm and implement it together, but each 
    # e-commerce site will be integrated slightly differently since it has 
    # different metrics
    # Example: EBay isn’t popular with product reviews, but it has seller reviews and percentage

    # Retrieve all objects from the database
    # queryset = Model.objects.all()

    # Retrieve a specific object based on a condition
    # single_object = Model.objects.get(some_field=some_value)

    # Filter objects based on certain conditions
    # filtered_objects = Model.objects.filter(another_field=another_value)
    
    #TO-DO: First, integrate with search bar to get product name a user input
    
    #TO-DO: Then, pass product name to Ahmed's function and get results from there
    #TO-DO: Finally, filter result based on this algorithm
    if request.method == 'POST':
        priceFactor = request.POST.get("priceFactor", None)
        customerReview = request.POST.get("customerReview", None)
        shipping = request.POST.get("shipping", None)
        returnPolicy = request.POST.get("returnPolicy", None)
        brandReputation = request.POST.get("brandReputation", None)
        min_price = 0
        max_price = float("infinity")
        if priceFactor == ">10000":
            min_price = 10000
            max_price = float("infinity")
        elif priceFactor == "<=10000":
            min_price = 3000
            max_price = 10000
        elif priceFactor == "<=3000":
            min_price = 1000
            max_price = 3000
        elif priceFactor == "<=1000":
            min_price = 500
            max_price = 1000
        elif priceFactor == "<=500":
            min_price = 0
            max_price = 500
        
        selected_shipping = ["Doesn't matter", "A couple week", "A week or so", "Amazon speeds", "Right now"]
        
        if shipping == "A couple week":
            selected_shipping = selected_shipping[1:]
        elif shipping == "A week or so":
            selected_shipping = selected_shipping[2:]
        elif shipping == "Amazon speeds":
            selected_shipping = selected_shipping[3:]
        elif shipping == "Right now":
            selected_shipping = selected_shipping[4:]
        
        #contact with database/api to get selected information based on simple algorithm
        product = Product.objects.filter(
                    price__range=(min_price, max_price),
                    customerReview=customerReview if customerReview is not None else '',
                    shippingTime__in=shipping if shipping is not None else [],
                    returnPolicy=returnPolicy if returnPolicy is not None else '',
                    brandReputation=brandReputation if brandReputation is not None else '',
        )
        
        #First render result_template and second sends http response to client(front end).
        return render(request, 'result_template.html', {'products': product})
        
        #TO-DO: pass it to Vincent's product data