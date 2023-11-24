from rest_framework import serializers
from .models import RouteModel


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        # fields = '__all__'
        fields = ['route_id', 'route_name', 'route_start_point', 'route_end_point','route_areas']






