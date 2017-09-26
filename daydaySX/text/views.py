from django.shortcuts import render, redirect
from text.models import *
from django.http import JsonResponse
from django.conf import settings
from text import tasks
from utlis.decorators import is_login


# Create your views here.


# 登陆
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = Passport.objects.verify(username, password=password)
        remember = request.POST.get('remember')

        if res:
            dic = {'res': 'yes'}
            if request.session.has_key('path'):
                dic['path'] = request.session['path']
            data = JsonResponse(dic)
            request.session['username'] = username
            request.session['id'] = res.id
            request.session['is_login'] = 'true'
            if remember == 'true':
                data.set_cookie('username', username, 14 * 24 * 3600)

        else:
            data = JsonResponse({'res': 'no'})
        return data

    else:
        if 'username' in request.COOKIES:
            name = request.COOKIES['username']
        else:
            name = ''
        return render(request, 'text/login.html', {'username': name})


@is_login
def logout(request):
    request.session.flush()
    return redirect('/goods/')


# 注册
def register(request):
    return render(request, 'text/register.html')


# 注册校验
def register_verify(request):
    Passport.objects.save_one_model(username=request.POST.get('user_name'), password=hex_has(request.POST.get('pwd')), email=request.POST.get('email'))
    tasks.my_send_email.delay('欢迎信息', '', settings.EMAIL_FROM, [request.POST.get('email')], '<h1>你好我是TDSun</h1>')
    return redirect('/login/')


# 用户名校验
def verify_username(request, name):
    user = Passport.objects.verify(name)
    if user:
        user = 1
    else:
        user = 0
    return JsonResponse({'user': user})



# 用户中心
@is_login
def user_center_info(request):
    dic = {'page': 'use'}
    return render(request, 'text/user_center_info.html', dic)


# 订单
@is_login
def user_center_order(request):
    dic = {'page': 'order'}
    return render(request, 'text/user_center_order.html', dic)


# 收货地址
@is_login
def user_center_site(request):
    pid = request.session.get('id')
    if request.method == 'GET':
        obj = Address.objects.get_one_moder(passport_id=pid,is_default=True)
        print(obj)
        dic = {'page': 'site', 'address': obj}
        return render(request, 'text/user_center_site.html', dic)
    else:
        recipient_name = request.POST.get('username')
        recipient_addr = request.POST.get('addre')
        recipient_phone = request.POST.get('phone')
        zip_code = request.POST.get('code')
        # 2.添加进数据库
        Address.objects.save_one_model(passport_id=pid,
                                        recipicent_name=recipient_name,
                                        recipicent_addr=recipient_addr,
                                        recipicent_phone=recipient_phone,
                                        zip_code=zip_code)
        return redirect('/use/site/')
