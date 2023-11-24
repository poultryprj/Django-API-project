from django.urls import path
from . import views

urlpatterns = [

    path('', views.UserList, name='user-list'),

    # path('users/<int:id>/', views.UserList, name='user-detail'),

    path('login/', views.UserLogin, name='user-login'),

   

]
