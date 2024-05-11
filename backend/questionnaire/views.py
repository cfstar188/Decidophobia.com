from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth import authenticate
# from . forms import CreateUserForm, CreateLoginForm
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
# import shop_search
import requests

#Below 6 lines are integration change -- attemping to merge 13 and 24, change made by Marvin
from django.shortcuts import render
from django.http import JsonResponse
from shop_search.search_engine import search_engine, elegant_print
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from shop_search.search_engine import search_engine



def hello_world(request):
    return render(request, 'temp.html')


def home(request):
    return render(request, 'home.html')

# def shopcart(request):
#     return render(request, 'shopcart.html')


def login(request):
    # form = CreateLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.user)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return JsonResponse({"message": "Login successful."}, status=status.HTTP_200_OK) 
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=status.HTTP_403_FORBIDDEN)

    return JsonResponse({"message": "Login failed."}, status=status.HTTP_400_BAD_REQUEST)



def logout(request):
    auth_logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        print("Form submitted!")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form submitted!")
            user = form.save()
            username = form.cleaned_data.get('username')
            auth_login(request, user)
            messages.success(request, f'Signup successful. Welcome, {username}!')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Signup failed. Please correct the errors in the form.')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def cart(request):
    if not (request.user.is_authenticated):
        return render(request, 'shopcart.html')
    uri = "http://127.0.0.1:8000/shopping-list/details"
    response = requests.get(uri)
    if response.status_code == 200:
        total_cost = 0.0
        for product in response.json():
            total_cost += product['product_price'] * product["quantity"]
        return render(request, 'shopcart.html', {'user_products': response.json, 'total_cost': total_cost})
    return render(request, 'shopcart.html')


def remove_from_cart(request, product_id):
    # product = get_object_or_404(ProductItem, pk=product_id)
    # if product.user == request.user:
    #     product.delete()
    return redirect('cart')

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

product6 = {
    "name": "iphone",
    "link": "https://example.com/gamingdeluxe",
    "image": "https://example.com/images/gamingdeluxe.jpg",
    "price": 1000000.99,
    "currency": "CAD",
    "score": 4.2
}

def settings(request):
    return render(request, 'settings.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            return redirect('home')  # Redirect to home page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# Switch to questionnaire page after user submit product/get product and pass it to product table
# Changed to filter, url is at filter.
def filter(request):
    """
    print("in search block")
    if request.method == 'GET':
        action = request.GET.get('action')
        
        # User chooses not to filter product
        if action == "search":
            product_name = request.GET.get("searchQ")
            
            # products_lst = search_engine.exec_search({"product_name" : product_name }) 
            products_lst = [product1, product2, product3, product4, product5]
            
            # Need to make a post request to vincent's next.js server so he can display product
            response = JsonResponse({"products": products_lst})
            # Add CORS headers directly to the response
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
            response["Access-Control-Allow-Credentials"] = "true"
            return response
        
        # User chooses to filter product
        elif action == "filter":
             """
    
    print("in filter block")
    
    if request.method == 'GET':
        # Get product name and stores it in session
        product_name = request.GET.get("searchQ")
        # render questionnaire.html directly
        #print("product name is :" + request.GET.get("searchQ"))
        print("product_name is " + product_name)
        
        return Response({
            'message': 'return product name to questionnaire page',
            'product_name': product_name
        }, status=status.HTTP_201_CREATED)

# normalize each product based on customer review. To be on a scale of 0 to 100
def normalize_products(bestbuy_products, ebay_products, kroger_products):
    if len(bestbuy_products) > 1:
        highest_score = 0
        lowest_score = float('inf')
        for bestbuy_product in bestbuy_products:
            bestbuy_products_review = float(bestbuy_product['metrics']["review_count"]) * float(bestbuy_product['metrics']["review_average"])
            if bestbuy_products_review < lowest_score:
                lowest_score = bestbuy_products_review
            if bestbuy_products_review > highest_score:
                highest_score = bestbuy_products_review
                
        # for ind in range(0, min(5, len(bestbuy_products))):
        #     print("bestbuy_product score: ", bestbuy_products[ind]['metrics']['review_average'], bestbuy_products[ind]['metrics']['review_count'])
        
        for bestbuy_product in bestbuy_products:
            bestbuy_products_review = float(bestbuy_product['metrics']["review_count"])  *  float(bestbuy_product['metrics']["review_average"])
            normalized_value = ((bestbuy_products_review - lowest_score) / (highest_score - lowest_score)) * 100
            bestbuy_product['metrics']['normalized_value'] = normalized_value
    elif len(bestbuy_products) == 1:
        bestbuy_products[0]['metrics']['normalized_value'] = 50 
        
    if len(ebay_products) > 1:
        highest_score = 0
        lowest_score = float('inf')
        for ebay_product in ebay_products:
            ebay_product_review = float(ebay_product['metrics']['feedback_score']) * float(ebay_product['metrics']['feedback_percentage'])
            if  float(ebay_product_review) < lowest_score:
                lowest_score = ebay_product_review
            if float(ebay_product_review) > highest_score:
                highest_score = ebay_product_review
            
        for ebay_product in ebay_products:
            ebay_product_review = float(ebay_product['metrics']['feedback_score']) * float(ebay_product['metrics']['feedback_percentage'])
            normalized_value = (( ebay_product_review - lowest_score) / (highest_score - lowest_score)) * 100
            ebay_product['metrics']['normalized_value'] = normalized_value
    elif len(ebay_products) == 1:
        ebay_products[0]['metrics']['normalized_value'] = 50 
    
    if len(kroger_products) > 1:
        highest_score = 0
        lowest_score = float('inf')
        for kroger_product in kroger_products:
            kroger_product_review = float(kroger_product['metrics']['price'])
            if  kroger_product_review < lowest_score:
                lowest_score = kroger_product_review
            if kroger_product_review > highest_score:
                highest_score = kroger_product_review
            
        for kroger_product in kroger_products:
            kroger_product_review = float(kroger_product['metrics']['price'])
            normalized_value = (( kroger_product_review - lowest_score) / (highest_score - lowest_score)) * 100
            kroger_product['metrics']['normalized_value'] = normalized_value
    elif len(kroger_products) == 1:
        kroger_products[0]['metrics']['normalized_value'] = 50 

def normalize_after_adjusting_based_on_brand_reputation(bestbuy_products, ebay_products, kroger_products):
    # apply brand reputation factor to product
    # best buy has product score 80.8 and ebay has product score 
    all_products = bestbuy_products + ebay_products + kroger_products
    for product in all_products:
        product['metrics']['normalized_value'] *= product['score']
        
    highest = 0
    lowest = float('inf')
    for product in all_products:
        if product['metrics']['normalized_value'] < lowest:
            lowest = product['metrics']['normalized_value']
        if product['metrics']['normalized_value'] > highest:
            highest = product['metrics']['normalized_value']
            
    # normalize to the scale of 0 to 100
    for product in all_products:
        product['metrics']['normalized_value'] = ((product['metrics']['normalized_value'] - lowest) / (highest - lowest)) * 100    
    
    return all_products

def customer_review_and_brand_reput_calibrate(interleaved_products, customer_review):
    print(customer_review)
    # sort products by ebay's feedback_score and feedback_percentage tomorrow
    bestbuy_products = [result for result in interleaved_products if result["shop"].lower() == "bestbuy"]
    ebay_products = [result for result in interleaved_products if result["shop"].lower() == "ebay"]
    kroger_products = [result for result in interleaved_products if result["shop"].lower() == "kroger"]
    
    # normalize products from different websites to be on the same scale
    normalize_products(bestbuy_products, ebay_products, kroger_products)
        
    # after applying the effects of different brand reputation, normalize the products to be on the same scale again
    normalized_products = normalize_after_adjusting_based_on_brand_reputation(bestbuy_products, ebay_products, kroger_products)
            
    sorted_and_normalized_products = sorted(normalized_products, key=lambda x: x["metrics"]['normalized_value'] , reverse=True)    

    # divide total number of products by 5
    num_of_products = 1 if (len(sorted_and_normalized_products)) // 5 == 0 else (len(sorted_and_normalized_products)) // 5

    # return products that satisfy the given customer review from high quality to lower quality. Unqualified products are removed 
    if(type(int(customer_review)) == 3):
        filter_result = sorted_and_normalized_products[0:num_of_products * (6 - int(customer_review))]
    else:
        return interleaved_products
    
    return filter_result


def questionnaire(request):
    #TO-DO: Pass user preferences to ahmed's function and he can do the filtering
    # products_lst = search_engine.exec_search({"product_name" : product_name })
    print("in questionnaire")
    
    if request.method == "GET":
        print("This is a GET request")
    elif request.method == "POST":
        print("This is a POST request")
    else:
        print("This is a different type of request")
        
    product_name = request.GET.get("searchQ", None)
    customer_review = request.GET.get("customerReview", None)
    price_factor = request.GET.get("priceFactor", None)
    shipping = request.GET.get("shipping", None)
    return_policy = request.GET.get("returnPolicy", None)
    brand_reputation = request.GET.get("brandReputation", None)
    
    print("this is productName")
    print(product_name)
    print("this is priceFactor")
    print(price_factor)
    print("this is customerReview")
    print(customer_review)
    print("this is shipping")
    print(shipping)
    print("this is returnPolicy")
    print(return_policy)
    print("this is brandReputation")
    print(brand_reputation)
    
    min_price = 0
    max_price = float("infinity")
    if price_factor == ">10000":
        max_price = float("infinity")
        min_price = 10000
    elif price_factor == "<=10000":
        max_price = 10000
        min_price = 3000
    elif price_factor == "<=3000":
        max_price = 3000
        min_price = 1000
    elif price_factor == "<=1000":
        max_price = 1000
        min_price = 500
    elif price_factor == "<=500":
        max_price = 500
        min_price = 0
    
    selected_shipping = ["Does not matter", "A couple week", "A week or so", "Amazon speeds", "Right now"]
    
    if shipping == "A couple week":
        selected_shipping = selected_shipping[1:]
    elif shipping == "A week or so":
        selected_shipping = selected_shipping[2:]
    elif shipping == "Amazon speeds":
        selected_shipping = selected_shipping[3:]
    elif shipping == "Right now":
        selected_shipping = selected_shipping[4:]
    
    print("before search engine")
    
    interleaved_products = search_engine({"item": product_name, "shops": ["ebay", "bestbuy", "kroger"]})
        
    # for item in interleaved_products:
    #     if item['shop'].lower() == "kroger":
    #         print(item, end="\n")
    print("after searching and before filtering")
    # for product in interleaved_products:
    #     print(product)
        
    #TO-DO: Finally, filter result based on the filtering algorithm
    # filtering algorithm prototype
    
    # filtering algorithm: apply price factor
    interleaved_products_cpy = interleaved_products[:]
    for product in interleaved_products:
        if(float(product['price']) > max_price or float(product['price']) < min_price):
            interleaved_products_cpy.remove(product)
    
    print("filtering 1, printing out products:")
    # for ind in range(0, 10):
    #     print(interleaved_products_cpy[ind], end="\n")
    
    # filtering algorithm: apply customer review and brand reputation
    # filtering algorithm: brand reputation. Src: https://www.axios.com/2023/05/23/corporate-brands-reputation-america
    print("Before applying customer review and brand reputation\n")
    interleaved_sorted_products = customer_review_and_brand_reput_calibrate(interleaved_products_cpy, customer_review)
    
    # print("filtering 2, printing out products: \n")
    # for ind in range(0, 10):
    #     print(interleaved_sorted_products[ind])
        
    #return jsonresponse to table
    print("before returning")
    response = JsonResponse({"products": interleaved_sorted_products})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
