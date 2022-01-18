from .serializers import *
from store.models import *
from rest_framework.generics import ListAPIView
from rest_framework import viewsets


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCatAPIView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCatSerializer


class UsersAPIView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
