from rest_framework import serializers
from .models import Category
from .models import Product



class Category_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class Product_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'image', 'description', 'price', 'available')