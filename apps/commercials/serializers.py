from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Product
        fields = '__all__'
        read_only_fields = 'id',


class StockMovementSerializer(serializers.ModelSerializer):

    item = ProductSerializer(source='product', read_only=True)

    class Meta:

        model = models.StockMovement
        fields = '__all__'
        read_only_fields = 'id',
