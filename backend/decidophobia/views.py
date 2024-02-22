from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import shop_search

#Below three lines are integration change -- attemping to merge 13 and 24, change made by Marvin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



def hello_world(request):
    return render(request, 'temp.html')

def home(request):
    return render(request, 'home.html')

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


#Below code are integration change -- attemping to merge 13 and 24, change made by Marvin

from enum import Enum

class product(Enum):
    itemName = 0
    itemLink = 1
    itemImg = 2
    itemPrice = 3
    sellerScore = 4
    sellerPercentage = 5

# TO-DO: First, integrate with search bar to get product name 

# Switch to questionnaire page after user submit product
def submit_product(request):
    if request.method == 'POST':
        request.session['product_name'] = request.POST.get("searchQ")
        # Get product name and send it to ahmed
        # Redirect to the 13_UX&UI.html page or render it directly
        return render(request, '13_UX&UI.html')

# Create your views here.
def questionnaire(request):
    
    # Retrieve all objects from the database
    # queryset = Model.objects.all()

    # Retrieve a specific object based on a condition
    # single_object = Model.objects.get(some_field=some_value)

    # Filter objects based on certain conditions
    # filtered_objects = Model.objects.filter(another_field=another_value)
    
    #TO-DO: Then, pass product name to Ahmed's function and get results from there
    product_name = request.session.get('product_name')    
    
    products_lst = search_engine.exec_search({product_name: "watch"})
    
    # Each dictionary has 6 attributes:
    # “name”, “link”, “image”, “price”, “currency”, “score”
    
    #TO-DO: Finally, filter result based on the filtering algorithm
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

        product_lst2 = products_lst[:]
        
        for i in range(0, len(products_lst)):
            product = products_lst[i]
            if(products_lst[i].price > max_price or products_lst[i].price < min_price):
                product_lst2.remove(product)
        
        sorted_products = sorted(product_lst2, key=lambda x: x['score'], reverse=True)

        num_of_products = 1 if len(sorted_products) // 5 == 0 else len(sorted_products) // 5
        
        filter_result = sorted_products[0:num_of_products*customerReview]
        
        #TO-DO: pass filter_result to Vincent's product data
        
        
        
        #contact with database/api to get selected information based on simple algorithm
        # product = Product.objects.filter(
        #             price__range=(min_price, max_price),
        #             customerReview=customerReview if customerReview is not None else '',
        #             shippingTime__in=shipping if shipping is not None else [],
        #             returnPolicy=returnPolicy if returnPolicy is not None else '',
        #             brandReputation=brandReputation if brandReputation is not None else '',
        # )
        
        # #First render result_template and second sends http response to client(front end).
        # return render(request, 'result_template.html', {'products': product})
        