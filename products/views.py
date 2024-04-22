from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Product, Order
from .serializer import CategorySerializer, ProductSerailizer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return  Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    

class CategoryDetailApiView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, id):
            category = get_object_or_404(Category, id=id)
            serializer = CategorySerializer(instance=category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            category = get_object_or_404(Category, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'Category not found!'
                }
            )
        else:
            category.delete()
            return Response(
                data={ProductSerailizer
                }
            )
         



class ProductApiView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerailizer(product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = ProductSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetailApiVew(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serailizer = ProductSerailizer(product)
        return Response(data=serailizer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerailizer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            product = get_object_or_404(Product, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'Product not found'
                }
            )
        else:
            product.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'Product successfully deleted'
                }
            )




class OrderApiView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderDetailApiView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            order = get_object_or_404(Order, id=id)
        except:
                return Response(
            data={
                'success': False,
                'message': 'Order not found'
            }
        )
        else:
            order.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'Order successfully deleted'
                }
            )