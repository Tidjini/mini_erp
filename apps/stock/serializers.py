from rest_framework import serializers

from . import models


class UniteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unite
        fields = '__all__'
        read_only_fields = 'id',


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SlugRelatedField(
        slug_field='name', many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = 'id',


class SubCategorySerializer(serializers.ModelSerializer):

    category_name = serializers.SlugRelatedField(
        source='category', slug_field='name', read_only=True)

    class Meta:
        model = models.SubCategory
        fields = '__all__'
        read_only_fields = 'id',


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
