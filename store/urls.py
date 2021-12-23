from django.urls import path
from .views import *

urlpatterns = [
    path('', log_in, name='login'),
    path('list', ProductListView.as_view(), name='home'),
    path('index/', index, name='index'),
    path('categories/', categories, name='categories'),
    path('category_add/', category_add, name='category_add'),
    path('products/', products, name='products'),
    path('product_add/', product_add, name='product_add'),
    path('product_edit/<int:id>', product_edit, name='product_edit'),
    path('subcat/', subcategory, name='subcat'),
    path('subcat_add/', subcat_add, name='subcat_add'),
]
