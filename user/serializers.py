from rest_framework import serializers
from .models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = '__all__'
        fields = ['user_id', 'user_name', 'user_mobile_no', 'user_alt_mobile_no','user_password', 'user_level']


