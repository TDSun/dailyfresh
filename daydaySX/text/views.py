from django.shortcuts import render,redirect

import templates
# Create your views here.


def index(request):
    return render(request,'text/index.html')

def login(request):
    return render(request,'text/login.html')

def register(request):
    return render(request,'text/register.html')

def register_verify(request):

    return redirect('/login/')

def cart(request):
    return render(request,'text/cart.html')

def detail(request):
    return render(request,'text/detail.html')

def list(request):
    return render(request,'text/list.html')

def place_order(request):
    return render(request,'text/place_order.html')

def user_center_info(request):
    return render(request,'text/user_center_info.html')

def user_center_order(request):
    return render(request,'text/user_center_order.html')

def user_center_site(request):
    return render(request,'text/user_center_site.html')

