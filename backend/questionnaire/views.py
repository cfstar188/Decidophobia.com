from django.shortcuts import render
# from . forms import CreateUserForm, CreateLoginForm
from django.http import JsonResponse, HttpResponseBadRequest

#Below three lines are integration change -- attemping to merge 13 and 24, change made by Marvin
from django.shortcuts import render
<<<<<<< Updated upstream
from django.http import HttpResponse, JsonResponse
from .models import Product
=======
>>>>>>> Stashed changes
import json
import requests
from django.urls import reverse

#Below code are integration change -- attemping to merge 13 and 24, change made by Marvin

from enum import Enum

class product(Enum):
    itemName = 0
    itemLink = 1
    itemImg = 2
    itemPrice = 3
    sellerScore = 4
    sellerPercentage = 5

# TO-DO: First, integrate with search bar to get product name. When user hits filter button on the home page, 

# Example product, for debugging purposes
product1 = {
    "name": "Laptop 1",
    "link": "https://example.com/laptop1",
    "image": "https://example.com/images/laptop1.jpg",
    "price": 999.99,
    "currency": "USD",
    "score": 4.5
}

product2 = {
    "name": "Smartphone X",
    "link": "https://example.com/smartphoneX",
    "image": "https://example.com/images/smartphoneX.jpg",
    "price": 799.99,
    "currency": "USD",
    "score": 4.2
}

product3 = {
    "name": "Headphones Pro",
    "link": "https://example.com/headphonespro",
    "image": "https://example.com/images/headphonespro.jpg",
    "price": 199.99,
    "currency": "USD",
    "score": 4.7
}

product4 = {
    "name": "Tablet Plus",
    "link": "https://example.com/tabletplus",
    "image": "https://example.com/images/tabletplus.jpg",
    "price": 499.99,
    "currency": "USD",
    "score": 4.3
}

product5 = {
    "name": "Gaming Console Deluxe",
    "link": "https://example.com/gamingdeluxe",
    "image": "https://example.com/images/gamingdeluxe.jpg",
    "price": 599.99,
    "currency": "USD",
    "score": 4.8
}

# Switch to questionnaire page after user submit product/get product and pass it to product table
def search(request):
    if request.method == 'GET':
        action = request.GET.get('submit')
        
        # User chooses not to filter product
        if action == "search":
            request.session['product_name'] = request.GET.get("searchQ")
            
            # products_lst = search_engine.exec_search({"product_name" : product_name })
                
            products_lst = [product1, product2, product3, product4, product5]
            
            # Need to make a post request to vincent's next.js server so he can display product
            table_url = reverse('table_url')
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({'products_lst': products_lst})
            response = requests.post(table_url, data=data, headers=headers)
            
        # User chooses to filter product
        elif action == "filter":
            
            # Get product name and stores it in session
            request.session['product_name'] = request.GET.get("searchQ")
            # render questionnaire.html directly
            print("product name is :" + request.GET.get("searchQ"))
            return render(request, 'questionnaire.html')

def questionnaire(request):
    
    #TO-DO: Pass user preferences to ahmed's function and he can do the filtering
    # products_lst = search_engine.exec_search({"product_name" : product_name })
    products_lst = [product1, product2, product3, product4, product5]
    
<<<<<<< Updated upstream
=======
    #TO-DO: Pass user preferences to ahmed's function and he can do the filtering
    product_name = request.session.get('product_name') 
    
>>>>>>> Stashed changes
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

        #TO-DO: Finally, filter result based on the filtering algorithm
        # filtering algorithm prototype
        product_lst2 = products_lst[:]
        for i in range(0, len(products_lst)):
            product = products_lst[i]
            if(products_lst[i].price > max_price or products_lst[i].price < min_price):
                product_lst2.remove(product)
        
        sorted_products = sorted(product_lst2, key=lambda x: x['score'], reverse=True)

        num_of_products = 1 if len(sorted_products) // 5 == 0 else len(sorted_products) // 5

        filter_result = sorted_products[0:num_of_products*customerReview]

<<<<<<< Updated upstream
        #return jsonresponse to table
        return JsonResponse(filter_result, safe=False)
    return JsonResponse(products_lst, safe=False)
    
=======
        filter_result["Access-Control-Allow-Origin"] = "*"  # Allow any domain
        filter_result["Access-Control-Allow-Methods"] = "GET, OPTIONS"  # Allowed methods
        filter_result["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"  # Allowed headers

        return JsonResponse(products_lst)
    
        
>>>>>>> Stashed changes
