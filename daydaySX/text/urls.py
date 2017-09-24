from django.conf.urls import url
from text import views

urlpatterns = [
    url(r'^$',views.index),

    url(r'^login/$',views.login),

    url(r'^register/$',views.register),
    url(r'^register_verify/$',views.register_verify),
    url(r'^verify/(\w+)/$',views.verify_username),

    url(r'^use/$',views.user_center_info),
    url(r'^use/order/$',views.user_center_order),
    url(r'^use/site/$',views.user_center_site),

    url(r'^car/$',views.car),

    url(r'^list/$',views.list),

    url(r'^detail/$',views.detail),

    url(r'^order/$',views.place_order),

]
