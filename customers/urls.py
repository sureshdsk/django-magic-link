from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.customers_home_page, name="customers-home"),
    url(r'^login/$',views.login_page, name="customers-login"),
]

