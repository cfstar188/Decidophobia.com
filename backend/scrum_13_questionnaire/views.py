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
    # Retrieve all objects from the database
    # queryset = Model.objects.all()

    # Retrieve a specific object based on a condition
    # single_object = Model.objects.get(some_field=some_value)

    # Filter objects based on certain conditions
    # filtered_objects = Model.objects.filter(another_field=another_value)
    
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
        
        # For sprint 2 which I will get result from ebay api and hopefully others
        # item_name = result[0][product.itemName.value]
        
        # item_link = result[0][product.itemLink.value]
        # item_img = result[0][product.itemImg.value]
        # item_price = result[0][product.itemPrice.value] 
        # seller_score = result[0][product.sellerScore.value]
        # seller_percentage = result[0][product.sellerPercentage.value]
        