"""
URL configuration for toiboss_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from menu.views import HomeView, ProductListView, ProductDetailView, RecipeDetailView, RecipesView
from public.views import PublicationsView, PublicationDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('products/', ProductListView.as_view(), name='products-url'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail-url'),
    path('recipes/', RecipesView.as_view(), name='recipes-url'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail-url'),
    path('publications/', PublicationsView.as_view(), name='publications-url'),
    path('publication/', PublicationDetailView.as_view(), name='publication-detail-url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
