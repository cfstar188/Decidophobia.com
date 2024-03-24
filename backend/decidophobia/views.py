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
from shop_search.search_engine import shop_search
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

def ebay_normalize(ebay_products, customer_review):
    # sort products by ebay's feedback_score and feedback_percentage tomorrow
    sorted_products = sorted(ebay_products, key=lambda x: x['feedback_score'] * x["feedback_percentage"], reverse=True)

    # divide total number of products by 5
    num_of_products = 1 if len(sorted_products) // 5 == 0 else len(sorted_products) // 5

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
    
    shop_name = "ebay"
    num_items = 10
    ebay_products = shop_search(product_name, num_items, shop_name)
    
    print("Before filtering")
    for product in ebay_products:
        print(product)
        
    #TO-DO: Finally, filter result based on the filtering algorithm
    # filtering algorithm prototype
    
    # filtering algorithm: price
    ebay_products2 = ebay_products[:]
    for product in ebay_products:
        if(float(product['price']) > max_price):
            ebay_products2.remove(product)
    
    print("filtering 1")
    for item in ebay_products2:
        print(item)
    
    # filtering algorithm: customer review
    ebay_product_result = ebay_normalize(ebay_products2, customer_review)

    print("After filtering")
    for result in ebay_product_result:
        print(result)
        
    #return jsonresponse to table
    response = JsonResponse({"products": ebay_product_result})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
