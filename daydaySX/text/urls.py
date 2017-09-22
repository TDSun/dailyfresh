from django.conf.urls import url
from text import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^register_verify/$',views.register_verify),
    url(r'^verify/(\w+)/$',views.verify_username),


]
