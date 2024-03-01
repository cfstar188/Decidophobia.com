from django.shortcuts import get_object_or_404, render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
import requests
from shopping_list.models import ShoppingListItem
from products.models import Product


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
            uri2 = "http://127.0.0.1:8000/shopping-list/add-item/"
            response = requests.post(uri, headers={"Key": 'decidophobiaAdmin'} ,json={"name": "Product 1", "company": "Company 1", "price": 100.32, "preview_picture": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLemIGXJw2Tn2UcEc43fsOt2Xie23XD180BUCrQAw6AkQZ97Iy_BiQ4g2RK36mTdZqG4rRIg"})
            response2 = requests.post(uri, headers={"Key": 'decidophobiaAdmin'} ,json={"name": "Product 2", "company": "Company 1", "price": 99, "preview_picture": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLemIGXJw2Tn2UcEc43fsOt2Xie23XD180BUCrQAw6AkQZ97Iy_BiQ4g2RK36mTdZqG4rRIg"})
            response3 = requests.post(uri, headers={"Key": 'decidophobiaAdmin'} ,json={"name": "Product 3", "company": "Company 1", "price": 8093, "preview_picture": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLemIGXJw2Tn2UcEc43fsOt2Xie23XD180BUCrQAw6AkQZ97Iy_BiQ4g2RK36mTdZqG4rRIg"})
            product_data = response.json()
            product_data2 = response2.json()
            product_data3 = response3.json()
            # print(product_data["id"])
            # response2 = requests.post(uri2, json={
            #     'product_id': product_data["id"],
            #     'quantity': 1
            # })
            # print(response)
            # print(response2)
            product = get_object_or_404(Product, pk=product_data["id"])
            ShoppingListItem.objects.create(user=request.user, product_id=product, quantity=1)
            product = get_object_or_404(Product, pk=product_data2["id"])
            ShoppingListItem.objects.create(user=request.user, product_id=product, quantity=1)
            product = get_object_or_404(Product, pk=product_data3["id"])
            ShoppingListItem.objects.create(user=request.user, product_id=product, quantity=1)
            return redirect('home')  
        else:
            print(form.errors)
            messages.error(request, 'Signup failed. Please correct the errors in the form.')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def cartview(request):
    if not (request.user.is_authenticated):
        return render(request, 'shopcart.html')
    uri = "http://127.0.0.1:8000/shopping-list/details/"
    response = requests.get(uri)
    total_cost = 0.0
    if response.status_code == 200:
        for product in response.json():
            total_cost += product['product_price'] * product["quantity"]
        print(response.json())
        return render(request, 'shopcart.html', {'user_products': response.json, 'total_cost': total_cost})
    return render(request, 'shopcart.html', {'total_cost': total_cost})


def remove_from_cart(request, product_id):
    uri = "http://127.0.0.1:8000/shopping-list/remove-item/"
    response = requests.delete(uri, json={"product_id": product_id})
    return redirect('cartview')


def update_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        new_quantity = request.POST.get('quantity')
        
        # Retrieve the shopping list item
        print(f"Item ID: {item_id}, New Quantity: {new_quantity}")
        # product = get_object_or_404(Product, pk=item_id)
        # shopping_list_item = get_object_or_404(ShoppingListItem, id=item_id)
        User = get_user_model()
    
        # Get the user instance or return None if user doesn't exist
        user_instance = get_object_or_404(User, username=request.user.username)
        
        # Retrieve the shopping list item for the user and product
        shopping_list_item = ShoppingListItem.objects.filter(user=user_instance, product_id=item_id).first()
        
        # Update the quantity
        shopping_list_item.quantity = new_quantity
        shopping_list_item.save()
        return redirect("http://127.0.0.1:8000/shopping-list/details/")
    else:
        return redirect('home')