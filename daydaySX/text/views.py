from django.shortcuts import render,redirect
from text.models import *
from django.http import JsonResponse
from django.conf import settings
from text import tasks
from utlis.decorators import is_login
# Create your views here.

# 首页
def index(request):
    dic = {'username':''}
    return render(request, 'text/index.html')

#登陆
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = Passport.objects.verify(username,password=password)
        remember = request.POST.get('remember')

        if res:
            dic = {'res':'yes'}
            if request.session.has_key('path'):
                dic['path'] = request.session['path']
            data = JsonResponse(dic)
            request.session['username'] = username
            request.session['id'] = res.id
            request.session['is_login'] = 'true'
            if remember == 'true':
                data.set_cookie('username',username,14*24*3600)

        else:
            data =  JsonResponse({'res':'no'})
        return data

    else:
        if 'username' in request.COOKIES:
            name = request.COOKIES['username']
        else:
            name = ''
        return render(request,'text/login.html',{'username':name})

@is_login
def logout(request):
    request.session.flush()
    return redirect('/')

#注册
def register(request):
    return render(request,'text/register.html')

# 注册校验
def register_verify(request):
    Passport.objects.add_one_passport(request.POST.get('user_name'),request.POST.get('pwd'),request.POST.get('email'))
    tasks.my_send_email.delay('欢迎信息','',settings.EMAIL_FROM,[request.POST.get('email')],'<h1>你好我是TDSun</h1>')
    return redirect('/login/')

# 用户名校验
def verify_username(request,name):
    user = Passport.objects.verify(name)
    if user:
        user = 1
    else:
        user = 0
    return JsonResponse({'user':user})

#购物车
@is_login
def car(request):
    return render(request,'text/cart.html')

@is_login
def detail(request):
    return render(request,'text/detail.html')


def list(request):
    return render(request,'text/list.html')

@is_login
def place_order(request):
    return render(request,'text/place_order.html')

@is_login
def user_center_info(request):
    return render(request,'text/user_center_info.html')

# 订单
@is_login
def user_center_order(request):
    return render(request,'text/user_center_order.html')


@is_login
def user_center_site(request):
    return render(request,'text/user_center_site.html')

