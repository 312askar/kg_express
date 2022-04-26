from django.urls import path
from .views import *

urlpatterns = [
    path('getSubcategory/', get_subcategories, name='get_subcategories'),
]
