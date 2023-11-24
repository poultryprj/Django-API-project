from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserModelSerializer
from django.http import JsonResponse



@api_view(['GET'])
def UserList(request):
    if request.method == 'GET':
        users = UserModel.objects.all()

        serializer = UserModelSerializer(users, many=True)
        response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": serializer.data
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    
    return JsonResponse({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": []
                }, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def UserLogin(request):
    if request.method == 'POST':
        user_name = request.data.get('user_name', None)
        user_password = request.data.get('user_password', None)

        if not user_name or not user_password:
            return JsonResponse({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": 'Invalid input. Both user_name and user_password are required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserModel.objects.get(user_name=user_name, user_password=user_password)

        except UserModel.DoesNotExist:
            return JsonResponse({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": []
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserModelSerializer(user)
        
        response_data = { 
            "message_text": "Success",
            "message_code": 1000,
            "message_data": [serializer.data]  
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)




