from django.shortcuts import render,redirect
from text.models import *
from django.http import HttpResponse,JsonResponse

import templates
# Create your views here.

# 首页
def index(request):
    return render(request,'text/index.html')

#登陆
def login(request):
    return render(request,'text/login.html')

#注册
def register(request):
    return render(request,'text/register.html')

# 注册校验
def register_verify(request):
    print(request.POST.get('pwd'))

    Passport.objects.add_one_passport(username=request.POST.get('user_name'),password=request.POST.get('pwd'),email=request.POST.get('email'))
    return redirect('/use/login/')

# 用户名校验
def verify_username(request,name):

    try:
        Passport.objects.get(username=name)
        user = 'no'
    except Exception:
        user = 'yes'
    return JsonResponse({'user':user})

#购物车
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

# 订单
def user_center_order(request):
    return render(request,'text/user_center_order.html')


def user_center_site(request):
    return render(request,'text/user_center_site.html')

