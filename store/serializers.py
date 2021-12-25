from rest_framework import serializers
from store.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'subcategory', 'category', 'code', 'name', 'model', 'datetime', 'description', 'type', 'image', 'price',
            'cr_on', 'cr_up', 'active')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'image', "cr_on", 'cr_up', 'active')


class SubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('category', 'name', 'image', "cr_on", 'cr_up', 'active')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "username", "first_name", "last_name", "avatar", "phone_number", 'address', 'info', 'language', 'cr_on',
            'cr_up', 'active')
