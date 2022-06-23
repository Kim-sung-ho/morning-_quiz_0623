from unicodedata import category
from rest_framework import serializers

from item.models import ItemOrder as ItemOrderModel
from item.models import Order as OrderModel
from item.models import Item as ItemModel
from item.models import Category as CategoryModel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ItemModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = OrderModel
        fields = "__all__"


class ItemOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    item = serializers.ReadOnlyField(source='item.name')

    class Meta:
        model = ItemOrderModel
        fields = "__all__"
