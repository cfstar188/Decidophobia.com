from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth import authenticate
# from . forms import CreateUserForm, CreateLoginForm
from rest_framework.response import Response
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



def hello_world(request):
    return render(request, 'temp.html')

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
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return Response({"message": "Login failed."}, status=status.HTTP_200_OK)



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

# normalize product score from bestbuy and ebay. To be on a scale of 0 to 100
def normalize(bestbuy_products, ebay_products):
    highest_score = 0
    lowest_score = float('inf')
    for bestbuy_product in bestbuy_products:
        if bestbuy_product["product_review"] < lowest_score:
            lowest_score = bestbuy_product["product_review"]
        if bestbuy_product["product_review"] > highest_score:
            highest_score = bestbuy_product["product_review"]
        
    for bestbuy_product in bestbuy_products:
        normalized_value = ((bestbuy_product['product_review'] - lowest_score) / (highest_score - lowest_score)) * 100
        bestbuy_product['product_review'] = normalized_value
    
    highest_score = 0
    lowest_score = float('inf')
    for ebay_product in ebay_products:
        if ebay_product["seller_score"] * ebay_product["seller_percentage"] < lowest_score:
            lowest_score = ebay_product["seller_score"] * ebay_product["seller_percentage"]
        if ebay_product["seller_score"] * ebay_product["seller_percentage"] > highest_score:
            highest_score = ebay_product["seller_score"] * ebay_product["seller_percentage"]
        
    # notice seller score is storing normalized value
    for ebay_product in ebay_products:
        normalized_value = ((ebay_product["seller_score"] * ebay_product["seller_percentage"] - lowest_score) / (highest_score - lowest_score)) * 100
        ebay_product['seller_score'] = normalized_value

def customer_review_and_brand_reput_calibrate(interleaved_products, customer_review):
    # sort products by ebay's feedback_score and feedback_percentage tomorrow
    bestbuy_products = [result for result in interleaved_products if result["shop"].lower() == "bestbuy"]
    ebay_products = [result for result in interleaved_products if result["shop"].lower() == "ebay"]
    
    normalize(bestbuy_products, ebay_products)
        
    # apply brand reputation factor to product
    # best buy has product score 80.8 and ebay has product score 
    for product in bestbuy_products:
        product['product_review'] *= 80.8
    for product in ebay_products:
        product["seller_score"] *= 72.1
        
    normalize(bestbuy_products, ebay_products)

    bestbuy_products.extend(ebay_products)
            
    sorted_products = sorted(bestbuy_products, key=lambda x: x["product_review"] if x['shop'] == "bestbuy" else x['seller_score'], reverse=True)    

    # divide total number of products by 5
    num_of_products = 1 if (len(sorted_products)) // 5 == 0 else (len(sorted_products)) // 5

    # return products that satisfy the given customer review from high quality to lower quality. Unqualified products are removed 
    filter_result = sorted_products[0:num_of_products * (6 - customer_review)]
    
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
    elif price_factor == "<=10000":
        max_price = 10000
    elif price_factor == "<=3000":
        max_price = 3000
    elif price_factor == "<=1000":
        max_price = 1000
    elif price_factor == "<=500":
        max_price = 500
    
    selected_shipping = ["Does not matter", "A couple week", "A week or so", "Amazon speeds", "Right now"]
    
    if shipping == "A couple week":
        selected_shipping = selected_shipping[1:]
    elif shipping == "A week or so":
        selected_shipping = selected_shipping[2:]
    elif shipping == "Amazon speeds":
        selected_shipping = selected_shipping[3:]
    elif shipping == "Right now":
        selected_shipping = selected_shipping[4:]
    
    interleaved_products = search_engine({"item": product_name, "shops": ["ebay", "bestbuy"]})
        
    print("after searching and before filtering")
    # for product in interleaved_products:
    #     print(product)
        
    #TO-DO: Finally, filter result based on the filtering algorithm
    # filtering algorithm prototype
    
    # filtering algorithm: apply price factor
    interleaved_products_cpy = interleaved_products[:]
    for product in interleaved_products:
        if(float(product['price']) > max_price):
            interleaved_products_cpy.remove(product)
    
    print("filtering 1")
    for item in interleaved_products_cpy:
        print(item)
    
    # filtering algorithm: apply customer review and brand reputation
    # filtering algorithm: brand reputation. Src: https://www.axios.com/2023/05/23/corporate-brands-reputation-america
    interleaved_sorted_products = customer_review_and_brand_reput_calibrate(interleaved_products_cpy, customer_review)
    
    print("After filtering")
    for result in interleaved_sorted_products:
        print(result)
        
    #return jsonresponse to table
    response = JsonResponse({"products": interleaved_sorted_products})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
