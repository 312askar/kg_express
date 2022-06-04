from rest_framework import serializers

from backend.apps.product.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]


class SubcategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'slug',
            'category'
        ]


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # subcategory = SubcategorySerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    # subcategories = SubcategorySerializer(read_only=True, many=True)
    subcategories = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'subcategories'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'image',
            'category',
            'subcategory',
        ]


