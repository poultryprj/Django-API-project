from django.shortcuts import render, HttpResponse
from .models import ShopModel

# Create your views here.

def ShopList(request):
    data = ShopModel.objects.all()
    print(data)
    return HttpResponse("Mayur")