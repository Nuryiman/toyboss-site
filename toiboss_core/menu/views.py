from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import Category, Product, Recipe


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductListView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        product_categories = Category.objects.prefetch_related('products').all()
        context = {
            'product_categories': product_categories
        }
        return context


class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        other_products = product.category.products.all().exclude(id=product.id)
        context = {
            'product': product,
            'other_products': other_products
        }
        return context


class RecipesView(TemplateView):
    template_name = 'recipes.html'


class RecipeDetailView(TemplateView):
    template_name = 'recipes-inner.html'

    def get_context_data(self, **kwargs):
        recipe = Recipe.objects.prefetch_related('products').get(id=kwargs['pk'])

        context = {
           'recipe': recipe
        }
        return context
