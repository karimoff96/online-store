from .serializers import *
from store.models import *
from rest_framework.generics import ListAPIView


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCatAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCatSerializer


class UsersAPIView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
