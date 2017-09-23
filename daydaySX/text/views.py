from django.shortcuts import render,redirect
from text.models import *
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import templates
from text import tasks
# Create your views here.

# 首页
def index(request):
    return render(request,'text/index.html')

#登陆
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = Passport.objects.verify(username,password=password)
        if res:
            return JsonResponse({'res':'yes'})
        else:
            return JsonResponse({'res':'no'})
    else:
        return render(request,'text/login.html')

#注册
def register(request):
    return render(request,'text/register.html')

# 注册校验
def register_verify(request):
    Passport.objects.add_one_passport(request.POST.get('user_name'),request.POST.get('pwd'),request.POST.get('email'))
    tasks.my_send_email.delay('欢迎信息','',settings.EMAIL_FROM,[request.POST.get('email')],'<h1>你好我是TDSun</h1>')
    return redirect('/use/login/')

# 用户名校验
def verify_username(request,name):
    user = Passport.objects.verify(name)
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

