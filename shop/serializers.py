from rest_framework import serializers
from .models import ShopRoute, ShopModel
from routes.serializers import RouteModelSerializer




class ShopModelSerializer(serializers.ModelSerializer):
    # shop_name = serializers.CharField(source='shop_id.shop_name', read_only=True)
    class Meta:
        model = ShopModel
        fields = '__all__'
        


class ShopRouteModelSerializer(serializers.ModelSerializer):
    # route_id = RouteModelSerializer(read_only=True)
    # shop_id = ShopModelSerializer(read_only=True)

    class Meta:
        model = ShopRoute
        fields = ['shop_route_id', 'route_id', 'shop_id', 'shop_order']
















# class ShopRouteModelSerializer(serializers.ModelSerializer):
#     shop_shoproute = serializers.StringRelatedField(source='shop_id', read_only=True)
#     route_shoproute = serializers.StringRelatedField(source='route_id', read_only=True)

#     class Meta:
#         model = ShopRoute
#         fields = ['shop_route_id', 'route_id', 'shop_order', 'shop_shoproute','route_shoproute']
