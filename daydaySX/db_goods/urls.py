from django.conf.urls import url
from db_goods import views

urlpatterns = [
    url(r'^$',views.index),

    url(r'^car/$',views.car),

    url(r'^list/$',views.list),

    url(r'^detail/(\d)/$',views.detail),

    url(r'^order/$',views.place_order),

]
