from django.contrib import admin

from menu.models import Product, Category, Recipe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', ]