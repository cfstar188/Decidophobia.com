from django.shortcuts import render, redirect
# from . forms import CreateUserForm, CreateLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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
