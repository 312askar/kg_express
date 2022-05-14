from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'id',
    ]
    prepopulated_fields = {
        'slug':('name',)
    }

@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'id',)
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('category',)
    search_fields = ('id', 'name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active',
    ]


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_link', 'image', 'created', 'updated')
    list_filter = ('created',)

