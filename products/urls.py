from django.urls import path
from .views import( ProductList , ProductDetales ,
                   CategoryList , CategoryDetale ,
                   FileList)

urlpatterns =[
    path('productlist/', ProductList.as_view() , name='product_list') ,
    path('productditale/<int:id>/' , ProductDetales.as_view() , name='product_ditale') ,

    path('categorylist/' , CategoryList.as_view()) ,
    path('categoryDetale/<int:id>/' , CategoryDetale.as_view()) , 

    path('filelist/<int:product_pk>' , FileList.as_view()) , 
]