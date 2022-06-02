from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from backend.apps.product.models import Category, SubCategory, Product
from .serializers import (
    CategorySerializer,
    SubcategorySerializer,
    ProductSerializer,
    CategoryDetailSerializer
)
# Create your views here.


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class SubcategoryListApiView(ListAPIView):
    serializer_class = SubcategorySerializer
    queryset = SubCategory.objects.all()


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
