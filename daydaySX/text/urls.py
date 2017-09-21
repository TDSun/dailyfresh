from django.conf.urls import url
from text import views

urlpatterns = [
    url(r'^use/index/$',views.index),
    url(r'^use/login/$',views.login),
    url(r'^use/register/$',views.register),
    url(r'^use/register_verify/$',views.register_verify),


]
