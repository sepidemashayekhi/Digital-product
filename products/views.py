from django.shortcuts import render
from django.http import Http404 

from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response

from .models import Category , File , Product
from .serializers import Categoryserializer , ProductSerializer


class ProductList(APIView):

    def get(self,request):
        try:
            products = Product.objects.all()
        except:
            raise  Http404
        print('[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]' , products)
        
        serialize = ProductSerializer(products , many=True ,context ={'request':request})
        print(serialize.data, 'ooooooooooooooooo')
        
        return Response(data=serialize.data)

