from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# import shop_search
import requests

#Below 6 lines are integration change -- attemping to merge 13 and 24, change made by Marvin
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import json
import requests
from django.urls import reverse




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

    return render(request, 'login.html')

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


#Below code are integration change -- attemping to merge 24 and 59 and 58, change made by Marvin

# TO-DO: First, integrate with search bar to get product name. When user hits filter button on the home page, 

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
    "name": "ASUS TUF F15 Gaming Laptop",
    "link": "https://www.amazon.ca/Display-i5-11400H-Processor-GeForce-FX506HF-AS51-CA/dp/B0BW115M5V/ref=asc_df_B0BW115M5V&mcid=f2f29127bb3d3faebd2d0aa8ab0e13c6?tag=bingshopdesk-20&linkCode=df0&hvadid=80058281925539&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=&hvtargid=pla-4583657845897036&psc=1",
    "image": "https://m.media-amazon.com/images/I/81dOiXqsD7L._AC_SL1500_.jpg",
    "price": 849.99,
    "currency": "CAD",
    "score": 4.5
}

product2 = {
    "name": "Samsung Galaxy Z Flip4 5G 128GB Graphite",
    "link": "https://www.amazon.ca/Samsung-Graphite-Snapdragon-charging-powershare/dp/B0B6N64R94/ref=sr_1_1?crid=1M07JI9B48CU3&dib=eyJ2IjoiMSJ9.UdUrImAw-jiGLkztt0kL2d1OcGZxPmdFuUZ4S9IAdJTB6L8MdxDEXyOA3srSgckSfUf7-WNQf_DmazYZ3dFRkG9cN_ItWZDRroRDSXv2WiWBCYwTTtFhd7EnmXr8EInIiZ-p2ff8R3lVHH6A9CCW6vATXxEjn6Rq36IFDexuHy1o6cSC7DWYElFDvBRX6okieMXRA3jE_mC8uPbXME5jjvr-C1N4hFlXSR-hwrj2SC5VcX4p9aJfk0mRt6zJqeyaZZM-gijA-b_0317MCaHFQv1GiX4dd5chTDGFIWSvv7M.j2vZwJbK8Jlt48nsDYCjxzjM5lDJS_GR_5lQDlaZubM&dib_tag=se&keywords=smartphone&qid=1708790162&s=electronics&sprefix=smartphone%2Celectronics%2C137&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    "image": "https://m.media-amazon.com/images/I/61ZXq2WgbsL._AC_SL1500_.jpg",
    "price": 644.99,
    "currency": "CAD",
    "score": 3.9
}

product3 = {
    "name": "BERIBES Bluetooth Headphones",
    "link": "https://www.amazon.ca/BERIBES-Bluetooth-Headphones-Microphone-Lightweight/dp/B09LYF2ST7/ref=sr_1_1?crid=1HBNU10097V5&dib=eyJ2IjoiMSJ9.wTD6IlbR_973L6HQPZjios7PuoX0GvpURWGw6wvS7W7R9BqySH_TYf0Qw1y-E7vNW9mAdvGnbd5Q_SlewGf2j6U3ETyeL2ASYJRBZbes74QJcUfb-oGLJXwQ0ooNrA0dpa3EFQdl-7WLbOZCCy6ENdqWwR-7ZIFB4mH5hiFCasw8uIRF_gHiRETNS8OPAAHjMBuZfY0HRcMwGY2UG__Zl2r8GLf9MkAfh1N1i-mcFE8FPty6j_GTuQD2AFKdHKYPx6CjUPbIdvoMGaUUOzWPQ3qoDD3OynGX5L8ODkXGiNA.WxN269SeJayjix4Lk9PemLFIREYwVkRLRXLlyV87yjM&dib_tag=se&keywords=headphones&qid=1708790277&s=electronics&sprefix=headphones%2Celectronics%2C129&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
    "image": "https://m.media-amazon.com/images/I/71F2ccIPPLL._AC_SL1500_.jpg",
    "price": 36.99,
    "currency": "CAD",
    "score": 4.4
}

product4 = {
    "name": "Amazon Fire HD 8 tablet",
    "link": "https://www.amazon.ca/All-new-Fire-HD-8-tablet/dp/B09BG5LXWJ/ref=sr_1_1?crid=13C67BZU0YRW&dib=eyJ2IjoiMSJ9.F7syKUU8K42fzYv0_9ZaK1ErmP6EcExqMg2tr0O6rNN26jwVxFDvRn2CTjN_R949LQmQRP5qkvS7-OU0hpd4mrPVLATgLzYx9i4GdozBrKAioliwbdvQDJmRVWsShmEU2JiibJTM1Ac59GlAVBcWf5qDGmp6fR7kw5yhBICVlFBLt9KFx1XSmy2-Zf3hlUJAwUHmsT7mqLn8aoN72cZgzN3-ppvHUCvWqKCmDVWbIGWNVSxvGWZxEOyeEiuK3eb-nxv4k-fp0HyTV9m2UjWST7jkpwgHqrro8oYGEa6WpmE.MtrtUbnNwCqPcxSn6yjxb2n4rIngPwbFuGnUqnMxaao&dib_tag=se&keywords=tablet&qid=1708790516&s=electronics&sprefix=tablet%2Celectronics%2C132&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    "image": "https://m.media-amazon.com/images/I/61ExVdn4flL._AC_SL1000_.jpg",
    "price": 119.99,
    "currency": "CAD",
    "score": 4.2
}

product5 = {
    "name": "Wireless Retro Game Console",
    "link": "https://www.amazon.ca/Wireless-Retro-Game-Console-Nostalgia/dp/B0CT61RP95/ref=sr_1_1?crid=3OF5TOPKYFLJO&dib=eyJ2IjoiMSJ9.lqKiIRWezja4S4aC5l4-3ruS8qcwHi2q6ptwc_iv7nBDZZheYNFxjBwBOYUylp9Z3ACwmdJrgP9nNipmmjRKlo91yXra_Yd5GFcvOh_5RQcby4hyM9u2MIvxo6PqN-kQaXAY6LBOEj7s1GdmFEWsgr7VYdQyj4Tn7cX40p5Xi54S0k7hDHPSEQxNAsK40kHlC-xdLku9X2AZEDYBTqQZxm9Tx0m_8-fQzSLjgFiE1e4OmjkIVEAE8iy_37JjQd-whk-AxHyvBRtEg7AKtUuHGVhN48Qx0eAagSChm4VmyU0.c-0IJFm9x2n-939s2D0QjEhDxMEY0UqNb3eqlQ2jPyg&dib_tag=se&keywords=gaming%2Bconsole&qid=1708790662&s=electronics&sprefix=gaming%2Bconsole%2Celectronics%2C103&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
    "image": "https://m.media-amazon.com/images/I/61CWpPLw6AL._AC_SL1319_.jpg",
    "price": 49.99,
    "currency": "CAD",
    "score": 4.7
}

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
        action = request.GET.get('action')
        # Get product name and stores it in session
        product_name = request.GET.get("searchQ")
        # render questionnaire.html directly
        #print("product name is :" + request.GET.get("searchQ"))
        return render(request, 'questionnaire.html')

def questionnaire(request):
    
    #TO-DO: Pass user preferences to ahmed's function and he can do the filtering
    # products_lst = search_engine.exec_search({"product_name" : product_name })
    products_lst = [product1, product2, product3, product4, product5]
    
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

        #return jsonresponse to table
        response = JsonResponse({"products": products_lst})

        # Add CORS headers directly to the response
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    response = JsonResponse({"products": products_lst})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
    