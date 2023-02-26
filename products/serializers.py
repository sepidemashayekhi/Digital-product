from rest_framework import serializers
from .models import Category,Product,File

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =[
            'title' ,
            'caption' ,
            'avatar' ,
        ]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields =[
            'title' ,
            'file',
        ]


class ProductSerializer(serializers.ModelSerializer):
    category=Categoryserializer(many=True)

    class Meta:
        model = Product
        fields =[
            'title' ,
            'caption',
            'avatar',
            'category',
        ]