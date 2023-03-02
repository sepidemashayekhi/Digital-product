from django.shortcuts import render
from django.http import Http404 

from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response

from .models import Category , File , Product
from .serializers import Categoryserializer , ProductSerializer , FileSerializer


class ProductList(APIView):

    def get(self,request):
        try:
            products = Product.objects.all()
        except:
            raise  Http404
        
        serialize = ProductSerializer(products , many=True ,context ={'request':request})
        
        return Response(data=serialize.data)
    
    def post(self , request):
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetales(APIView):
    def _get_object_(self , id):
        try:
            product = Product.objects.get(pk=id)
            return product
        except:
            raise Http404

    def get(self , request , id ):
        
        product =self._get_object_(id)
        serializer = ProductSerializer(product , context ={
            'request':request
        })
        print('llllllllllllllllll')
        return Response(serializer.data)
    
    def put(self, request , id):
        product = self._get_object_(id)
        serializer = ProductSerializer(product , request.data)
        if serializer.is_valid():
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , id):
        product = self._get_object_(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    def get(self , request):
        try:
            categories = Category.objects.all()
        except:
            raise Http404
        serializer =Categoryserializer(categories , many =True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
    def post(self , request) :
        serializer = Categoryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_204_NO_CONTENT)
    
class CategoryDetale(APIView):
    def _get_object_(self, id):
        try:
            category = Category.objects.get(pk =id)
            return category
        except:
            raise Http404
    
    def get(self , request ,id ):
        category = self._get_object_(id)
        serializer = Categoryserializer(category,context ={
            'request':request
        }) 
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self ,request , id):
        category = self._get_object_(id)
        serializer =Categoryserializer(category , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request , id):
        category = self._get_object_(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FileList(APIView):
    def get(self , request , product_pk):
        try:
            file = File.objects.filter(product_id = product_pk)

        except:
            raise Http404
        serializer = FileSerializer(file , many= True , context={
            'request':request
        })

        return Response(serializer.data ,status=status.HTTP_200_OK)
    