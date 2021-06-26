from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from .forms import OrderItemForm


# Create your views here.

# /----- Views for signup -----/
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already used")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)

                messages.info(request, "User created. Login now")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'html/register.html')


# /----- Views for Signin -----/
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong username or password")
            return redirect('login')
    else:
        return render(request, 'html/login.html')


# /----- Views for Logout -----/
def logout(request):
    auth.logout(request)
    return redirect('/')


# /----- Views for Homepage -----/
def home(request):
    club_jersey = ClubJerseyDetails.objects.all().order_by('-added_time')[:4]
    national_jersey = NTJerseyDetails.objects.all().order_by('-added_time')[:4]

    return render(request, 'html/home.html', {'club_jersey': club_jersey, 'national_jersey': national_jersey})


# /----- Views for Club jersey page -----/
def club(request):
    club_jersey = ClubJerseyDetails.objects.all().order_by('-added_time')
    paginator = Paginator(club_jersey, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/club.html', {'page_obj': page_obj})
    # return render(request, 'html/club.html', {'jerseys': jerseys})


# /----- Views for National jersey page -----/
def country(request):
    national_jersey = NTJerseyDetails.objects.all().order_by('-added_time')
    paginator = Paginator(national_jersey, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/country.html', {'page_obj': page_obj})
    # return render(request, 'html/country.html', {'NTjerseys': NTjerseys})


# /----- Views for Search -----/
def search_results(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        page_obj = ClubJerseyDetails.objects.all().filter(title__icontains=searched)
        page_obj1 = NTJerseyDetails.objects.all().filter(title__icontains=searched)

        return render(request, 'html/search_results.html',
                      {'searched': searched, 'page_obj': page_obj, 'page_obj1': page_obj1})
    else:
        return render(request, 'html/search_results.html', {})


# /----- Views for National jersey details page -----/
def national_jersey_details(request, national_jersey_id):
    national_jersey = NTJerseyDetails.objects.get(pk=national_jersey_id)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.save()

        if request.method == 'POST':
            form = OrderItemForm(request.POST, request.FILES)
            if form.is_valid():
                orderitem = form.save(commit=False)
                orderitem.national_jersey = national_jersey
                orderitem.order_id = order.id
                orderitem.save()

                return redirect('cart')
        else:
            form = OrderItemForm()

    return render(request, 'html/national_jersey_details.html', {'form': form, 'national_jersey': national_jersey})


# /----- Views for Club jersey details page -----/
def club_jersey_details(request, club_jersey_id):
    club_jersey = ClubJerseyDetails.objects.get(pk=club_jersey_id)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.save()

        if request.method == 'POST':
            form = OrderItemForm(request.POST, request.FILES)
            if form.is_valid():
                orderitem = form.save(commit=False)
                orderitem.club_jersey = club_jersey
                orderitem.order_id = order.id
                orderitem.save()

                return redirect('cart')
        else:
            form = OrderItemForm()

    return render(request, 'html/club_jersey_details.html', {'form': form, 'club_jersey': club_jersey})


# /----- Views for Cart page -----/
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'html/cart.html', context)


# /----- Views for Checkout page -----/
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'html/checkout.html', context)


# def updateItem(request):
#     data = json.loads(request.body)
#     jerseyId = data['jerseyId']
#     action = data['action']
#
#     print('action:', action)
#     print('jerseyId:', jerseyId)
#
#     customer = request.user.customer
#     national_jersey = NTJerseyDetails.objects.get(id=jerseyId)
#     order, created = Order.objects.get_or_create(customer=customer)
#     orderItem, created = OrderItem.objects.create(order=order, national_jersey=national_jersey)
#     orderItem.save()
#
#     return JsonResponse('Item is added', safe=False)




