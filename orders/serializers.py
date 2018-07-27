from rest_framework import serializers
from .models import Order, OrderItem
from shop.models import Product

class Order_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  'city']

# class Order_Item_Serializer(serializers.ModelSerializer):
#
#     order = Order_Serializer()
#
#     class Meta:
#         model = OrderItem
#         fields = ['order', 'product', 'price', 'quantity']