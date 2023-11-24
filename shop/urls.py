from django.urls import path
from . import views

urlpatterns = [

    path('', views.ShopList, name='route_list'),
    

   

]
