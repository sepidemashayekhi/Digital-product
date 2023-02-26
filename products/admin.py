from django.contrib import admin
from .models import Product,Category,File

@admin.register(Category)
class CtegoryInline(admin.ModelAdmin):
    list_display=[
        'parent',
        'title' ,
        'published_time',
    ]
    list_filter =[
        'parent',
        'published_time',

    ]

    search_fields=[
        'title' ,
    ]

class FileInLineAdmin(admin.StackedInline):
    model =File
    fields =[
        'title' , 
        'file' , 
    ] 
    extra = 0




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','title' , 'published_time']
    list_filter =[
        'published_time'
    ]
    search_fields =[
        'title'
    ]
    filter_horizontal=['category']
    inlines=[FileInLineAdmin]

