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


class TierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tier
        fields = '__all__'
        read_only_fields = 'id',



class PaymentSerializer(serializers.ModelSerializer):
    iter_item = TierSerializer(source='tier', read_only = True)

    class Meta:
        model = models.Payment
        fields = '__all__'
        read_only_fields = 'id',