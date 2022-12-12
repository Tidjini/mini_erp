from rest_framework import serializers

from . import models


class ThirdSerializer(serializers.ModelSerializer):

    balance = serializers.ReadOnlyField()

    class Meta:
        model = models.Third
        fields = '__all__'
        read_only_fields = 'id',


class PaymentSerializer(serializers.ModelSerializer):
    tier_item = ThirdSerializer(source='third', read_only=True)

    class Meta:
        model = models.Payment
        fields = '__all__'
        read_only_fields = 'id',
