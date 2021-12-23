from .serializers import *
from store.models import *
from rest_framework.generics import ListAPIView


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
