from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import RouteModel
from shop.models import ShopRoute
from .serializers import RouteModelSerializer
from shop.serializers import ShopRouteModelSerializer

# Create your views here.

@api_view(['GET'])
def RouteList(request):
    if request.method == 'GET':
        try:
            users = RouteModel.objects.all()
            print(users)
        except RouteModel.DoesNotExist:
             return JsonResponse({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": [],
                }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RouteModelSerializer(users, many=True)
        response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": serializer.data
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    
    
    return JsonResponse({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": [],
                }, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def RouteUnderShop(request,pk):
    if request.method == 'GET':
        try: 
            selected_route_id = RouteModel.objects.get(route_id=pk)
            shopList = ShopRoute.objects.filter(route_id=selected_route_id)
            print(shopList)

            serializer = ShopRouteModelSerializer(shopList, many=True)
            response_data = {
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": serializer.data
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        
        except RouteModel.DoesNotExist:
             return JsonResponse({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": [],
                }, status=status.HTTP_404_NOT_FOUND)
    
    return JsonResponse({"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
