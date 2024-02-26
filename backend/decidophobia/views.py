from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import requests

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
            uri = "http://127.0.0.1:8000/products/create-product/"
            requests.post(uri, headers={"Key": 'decidophobiaAdmin'} ,json={"name": "Product 1", "company": "Company 1", "price": 100.32, "preview_picture": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLemIGXJw2Tn2UcEc43fsOt2Xie23XD180BUCrQAw6AkQZ97Iy_BiQ4g2RK36mTdZqG4rRIg"})
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
    uri = "http://127.0.0.1:8000/shopping-list/details/"
    response = requests.get(uri)
    total_cost = 0.0
    if response.status_code == 200:
        for product in response.json():
            total_cost += product['product_price'] * product["quantity"]
        return render(request, 'shopcart.html', {'user_products': response.json, 'total_cost': total_cost})
    return render(request, 'shopcart.html', {'total_cost': total_cost})


def remove_from_cart(request, product_id):
    uri = "http://127.0.0.1:8000/shopping-list/remove-item/"
    response = requests.delete(uri, json={"product_id": product_id})
    return redirect('cart')


def update_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                try:
                    uri = "http://127.0.0.1:8000/shopping-list/change-quantity/"
                    response = requests.put(uri, json={"product_id": product_id, "quantity": int(value)})
                except Exception as e:
                    continue 
        return redirect('cart')
    else:
        return redirect('cart')