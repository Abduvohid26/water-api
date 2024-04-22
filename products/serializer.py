from .models import Category, Product, Order
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']



class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'size', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  ['id', 'username', 'product', 'category', 'phone_number', 'address', 'count', 'status']

