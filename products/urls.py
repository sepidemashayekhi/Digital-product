from django.urls import path
from .views import( ProductList , ProductDetales ,
                   CategoryList , CategoryDetale ,
                   FileList)

urlpatterns =[
    path('productlist/', ProductList.as_view() , name='product_list') ,
    path('productditale/<int:id>/' , ProductDetales.as_view() , name='product_ditale') ,

    path('categorylist/' , CategoryList.as_view()) ,
    path('categoryDetale/' , CategoryDetale.as_view()) , 

    path('filelist/' , FileList.as_view()) , 
]