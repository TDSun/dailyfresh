from django.shortcuts import render
from utlis.decorators import is_login
from db_goods.models import Goods

# Create your views here.
# 首页
def index(request):
    obj = Goods.objects.get_goods_num_byorder(goods_type_id=1,num=4)
    objn = Goods.objects.get_goods_num_byorder(goods_type_id=1,num=3,sort='new')
    obj2 = Goods.objects.get_goods_num_byorder(goods_type_id=2,num=4)
    objn2 = Goods.objects.get_goods_num_byorder(goods_type_id=2,num=3,sort='new')
    dic = {'obj': obj,'objn':objn,'obj2':obj2,'objn2':objn2}
    return render(request, 'text/index.html',dic)

# 购物车
@is_login
def car(request):
    return render(request, 'text/cart.html')


# 商品详情
@is_login
def detail(request,pid):
    goods = Goods.objects.get_one_goods_image(id=pid)
    goods_new = Goods.objects.get_goods_num_byorder(num=2,sort='new',goods_type_id=goods.goods_type_id)
    return render(request, 'text/detail.html',{'goods':goods,'goods_new':goods_new})

# 商品列表
def list(request):
    return render(request, 'text/list.html')


@is_login
def place_order(request):
    return render(request, 'text/place_order.html')

