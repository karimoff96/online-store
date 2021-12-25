from django.urls import path
from .views import *
from .serializerviews import *

urlpatterns = [
    path('', log_in, name='login'),
    path('index/', index, name='index'),
    path('categories/', categories, name='categories'),
    path('category_add/', category_add, name='category_add'),
    path('category_edit/<int:id>', category_edit, name='category_edit'),
    path('category_delete/<int:id>', category_delete, name='category_delete'),
    path('products/', products, name='products'),
    path('product_add/', product_add, name='product_add'),
    path('product_edit/<int:id>', product_edit, name='product_edit'),
    path('product_delete/<int:id>', product_delete, name='product_delete'),
    path('subcat/', subcategory, name='subcat'),
    path('subcat_add/', subcat_add, name='subcat_add'),
    path('subcat_edit/<int:id>', subcat_edit, name='subcat_edit'),
    path('subcat_delete/<int:id>', subcat_delete, name='subcat_delete'),

    # serializer_Part

    path('productapi/', ProductAPIView.as_view()),
    path('categoryapi/', CategoryAPIView.as_view()),
    path('subcatyapi/', SubCatAPIView.as_view()),
    path('usersapi/', UsersAPIView.as_view()),
]
