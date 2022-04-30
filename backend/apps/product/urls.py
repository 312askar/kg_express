from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubcategory/', get_subcategories, name='get_subcategories'),
    path('list/product/', ProductListView.as_view(), name='product_list')
]
