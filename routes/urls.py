from django.urls import path
from . import views

urlpatterns = [

    path('', views.RouteList, name='route_list'),
    path('<int:pk>/', views.RouteUnderShop, name='route_under_shop'),  

]
