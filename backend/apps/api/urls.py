from django.urls import path
from .views import CategoryListApiView, SubcategoryListApiView, ProductListApiView, CategoryDetailApiView


urlpatterns = [
    path('category_list/', CategoryListApiView.as_view()),
    path('subcategory_list/', SubcategoryListApiView.as_view()),
    path('product_list/', ProductListApiView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailApiView.as_view())
]
