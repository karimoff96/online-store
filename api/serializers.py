from rest_framework import serializers
from store.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code', 'name', 'model', 'datetime', 'description', 'type', 'image', 'price')