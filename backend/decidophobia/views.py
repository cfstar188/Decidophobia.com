from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth import authenticate
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

def questionnaire(request):
    #TO-DO: Pass user preferences to ahmed's function and he can do the filtering
    # products_lst = search_engine.exec_search({"product_name" : product_name })
    print("in questionnaire")
    priceFactor = request.POST.get("priceFactor", None)
    #customerReview = request.POST.get("customerReview", None)
    shipping = request.POST.get("shipping", None)
    returnPolicy = request.POST.get("returnPolicy", None)
    brandReputation = request.POST.get("brandReputation", None)
    print("this is priceFactor\n")
    print(priceFactor)
    min_price = 0
    max_price = float("infinity")
    if priceFactor == ">10000":

        max_price = float("infinity")
    elif priceFactor == "<=10000":
        max_price = 10000
    elif priceFactor == "<=3000":
        max_price = 3000
    elif priceFactor == "<=1000":
        max_price = 1000
    elif priceFactor == "<=500":
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
    
    # Input:
    # The function 'shop_search' takes in the following parameters:

    #     shop_name: string 
    #     ** This is the name of the shopping site you want to search. Currently, only
    #     "ebay" is supported (case insensitive)
        
    #     item_name: string 
    #     ** This is the name of the item you want to search for
        
    #     num_items: int
    #     ** This is the number of items you want returned back
        
    #     force_new_token = False
    #     ** You shouldn't need to pass this in, ever. This is more so for testing; if 
    #     you need an authorization token generated, you can set this to true.

    # Output:
    # The function returns a list of dictionaries. Each dictionary has the following keys:

    #     dict['shop']: string
    #     ** This is the name of the shop that was searched
        
    #     dict['name']: string
    #     ** This is the name of the item you want to search for
        
    #     dict['link']: string
    #     ** This is the link to the product on the shop's website
        
    #     dict['image']: string
    #     ** This is a link to the product image
        
    #     dict['price']: float
    #     ** This is the price of the product in USD
        
    #     dict['score']: int
    #     This is our unique score that we give to items (it defaults to 100 currently)

    shop_name = "ebay"
    item_name = request.POST.get('product_name')
    print("item_name:" + item_name)
    num_items = 10
    products_lst = shop_search(item_name, num_items, shop_name)

    # print("Before filtering")
    # for i in range(len(products_lst)):
    #     print(products_lst[i])
        
    #TO-DO: Finally, filter result based on the filtering algorithm
    # filtering algorithm prototype
    product_lst2 = products_lst[:]
    for i in range(0, len(products_lst)):
        product = products_lst[i]
        if(float(product['price']) > max_price):
            product_lst2.remove(product)
    
    # print("filtering 1")
    # for i in range(len(product_lst2)):
    #     print(product_lst2[i])
    
    sorted_products = sorted(product_lst2, key=lambda x: x['score'], reverse=True)

    num_of_products = 1 if len(sorted_products) // 5 == 0 else len(sorted_products) // 5

    filter_result = sorted_products[0:num_of_products] #*customerReview]
    
    print("After filtering")
    for i in range(len(filter_result)):
        print(filter_result[i])
        
    #return jsonresponse to table
    response = JsonResponse({"products": filter_result})

    # Add CORS headers directly to the response
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
    response["Access-Control-Allow-Credentials"] = "true"
    return response